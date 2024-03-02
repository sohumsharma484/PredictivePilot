use actix_multipart::{
    form::{
        tempfile::{TempFile, TempFileConfig},
        MultipartForm,
    },
    Multipart,
};
use actix_web::{get, patch, post, middleware, web, App, Error, HttpResponse, HttpServer, Responder};
// Will most likely use following later
// use futures_util::TryStreamExt as _;
// use uuid::Uuid;
// use validator::Validate;

#[get("/")]
async fn get_home() -> impl Responder{
    HttpResponse::Ok().body("Welcome to the home page of PredictivePilot!")
}

#[derive(Debug, MultipartForm)]
struct UploadForm {
    #[multipart(rename = "file")]
    files: Vec<TempFile>,
}

async fn save_files(
    MultipartForm(form): MultipartForm<UploadForm>,
) -> Result<impl Responder, Error> {
    for f in form.files {
        let path = format!("./data/{}", f.file_name.unwrap());
        log::info!("saving to {path}");
        f.file.persist(path).unwrap();
    }

    Ok(HttpResponse::Ok())
}

// Loads HTML for the upload form
async fn index() -> HttpResponse {
    let html = r#"<html>
        <head><title>Upload Test</title></head>
        <body>
            <form target="/" method="post" enctype="multipart/form-data">
                <input type="file" multiple name="file"/>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>"#;

    HttpResponse::Ok().body(html)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init_from_env(env_logger::Env::new().default_filter_or("info"));

    log::info!("creating temporary upload directory");
    std::fs::create_dir_all("./data")?;

    log::info!("starting HTTP server at http://localhost:8080");

    HttpServer::new(|| {
        App::new()
            .wrap(middleware::Logger::default())
            .app_data(TempFileConfig::default().directory("./data"))
            .service(
                web::resource("/upload")
                    .route(web::get().to(index))
                    .route(web::post().to(save_files)),
            )
            .service(get_home)
    })
    .bind(("127.0.0.1", 8080))?
    .workers(2)
    .run()
    .await
}




#[cfg(test)]
mod tests {
    use super::*;
    use actix_web::{test, web, App};
    use bytes::Bytes;


    #[actix_web::test]
    async fn test_get_home() {
        let mut app = test::init_service(
            App::new()
            .wrap(middleware::Logger::default())
            .app_data(TempFileConfig::default().directory("./data"))
            .service(
                web::resource("/upload")
                    .route(web::get().to(index))
                    .route(web::post().to(save_files)),
            )
            .service(get_home)
        ).await;

        let req = test::TestRequest::get().uri("/").to_request();
        let resp = test::call_service(&mut app, req).await;

        // Check if response is successful
        assert!(resp.status().is_success());

        // Check if response is correct
        let result = test::read_body(resp).await;
        assert_eq!(result, Bytes::from_static(b"Welcome to the home page of PredictivePilot!"));
    }

    #[actix_web::test]
    async fn test_index() {
        let mut app = test::init_service(
            App::new()
            .wrap(middleware::Logger::default())
            .app_data(TempFileConfig::default().directory("./data"))
            .service(
                web::resource("/upload")
                    .route(web::get().to(index))
                    .route(web::post().to(save_files)),
            )
            .service(get_home)
        ).await;

        let req = test::TestRequest::get().uri("/upload").to_request();
        let resp = test::call_service(&mut app, req).await;

        // Check if response is successful
        assert!(resp.status().is_success());
    }
}

