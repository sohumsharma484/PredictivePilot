use pyo3::prelude::*;
use pyo3::types::PyModule;
use std::collections::HashMap;

struct MLModule {
    filename: String,
    methods: HashMap<String, Py<PyAny>>,
} 

impl MLModule {
    fn new(filename: &str) -> MLModule {
        Python::with_gil(|py| -> PyResult<MLModule> {
            let module = PyModule::from_code(
                py,
                &std::fs::read_to_string(filename).unwrap(),
                filename,
                "ml_suggest"
            )?;
            let mut methods_map = HashMap::new();
            for (k, v) in module.dict().iter() {
                if v.get_type().name()? == "function" {
                    methods_map.insert(k.to_string(), v.into_py(py));
                }
            };

            Ok(MLModule {
                filename: filename.to_string(),
                methods: methods_map,
            })
        }).unwrap()
    }

    fn get_methods(&self) -> &HashMap<String, Py<PyAny>> {
        &self.methods
    }

    fn get_filename(&self) -> &str {
        &self.filename
    }

}



#[cfg(test)]
mod tests {
    use super::*;


    #[test]
    fn test_call_ml_suggest() {
        let ml_module_name = "src/ml_suggest/linreg.py";
        let ml_module = MLModule::new(ml_module_name);  
        let methods = ml_module.get_methods();
        println!("{:?}", methods);
    }
}
