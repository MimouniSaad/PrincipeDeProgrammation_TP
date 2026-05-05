
    // SOAP : Simple Object Access Protocol ....
// JAX-WS (Java Annotation XML for Web Service)
// JAXB (Java Architecture XML Binding)

// URL : Uniform Resource Locator
// URN : Uniform Resource Name
// URI : Uniform Resource Identifier ...
// URN + URL = URI

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

    @WebService(targetNamespace = "https://www.polytech.fr")
    public class MonServiceWeb {
        @WebMethod(operationName = "convertir")
        public double conversion(double mt){
            return mt * 0.9;
        }

        public double somme(@WebParam(name= "parametre1") double a, double b){
            return a+b;
        }

        public Etudiant getEtudiant(int identifiant){
            return new Etudiant(1,"Mario", 19);
        }

    }

