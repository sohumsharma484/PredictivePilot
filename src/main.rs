use actix_web::{get, patch, post, HttpResponse, HttpServer, Responder, App, web::Json, web::Path, web::Data};
use validator::Validate;
use actix_web::web;

#[get("/")]
async fn get_home() -> impl Responder{
    HttpResponse::Ok().body("Welcome to the home page of PredictivePilot!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Create instance of server
    HttpServer::new(move || {
        App::new()
            .service(get_home)
            // .route("/", web::get().to(get_home))
    })
    .bind("127.0.0.1:8080")?
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
                .service(get_home),
        ).await;

        let req = test::TestRequest::get().uri("/").to_request();
        let resp = test::call_service(&mut app, req).await;

        // Check if response is successful
        assert!(resp.status().is_success());

        // Check if response is correct
        let result = test::read_body(resp).await;
        assert_eq!(result, Bytes::from_static(b"Welcome to the home page of PredictivePilot!"));
    }
}