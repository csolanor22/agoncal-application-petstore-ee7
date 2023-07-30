package org.agoncal.application.petstore.client;

import org.agoncal.application.petstore.model.Category;
import org.agoncal.application.petstore.model.Country;

import javax.ws.rs.client.*;
import javax.ws.rs.core.GenericType;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.List;

public class BackendPython {
    private static final String REST_URI_COUNTRY
        = "http://127.0.0.1:5000/country";
    private static final String REST_URI_CATEGORY
        = "http://127.0.0.1:5001/category";

    private Client client = ClientBuilder.newClient();
    
    public List<Country> getCountries(){
        return client
            .target(REST_URI_COUNTRY)
            .request(MediaType.APPLICATION_JSON)
            .get(new GenericType<List<Country>>() {});
    }

    public Country getCountryById(Long id){
        return client
            .target(REST_URI_COUNTRY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .get(Country.class);
    }
    public Response saveCountry(Country country){
        return client
            .target(REST_URI_COUNTRY)
            .request(MediaType.APPLICATION_JSON)
            .post(Entity.entity(country, MediaType.APPLICATION_JSON));
    }

    public Response updateCountry(Long id, Country country){
        return client
            .target(REST_URI_COUNTRY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .put(Entity.entity(country, MediaType.APPLICATION_JSON));
    }

    public String deleteCountry(Long id){
        return client
            .target(REST_URI_COUNTRY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .delete(String.class);
    }

    //Categories methods
    public List<Category> getCategories(){
        return client
            .target(REST_URI_CATEGORY)
            .request(MediaType.APPLICATION_JSON)
            .get(new GenericType<List<Category>>() {});
    }

    public Category getCategoryById(Long id){
        return client
            .target(REST_URI_CATEGORY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .get(Category.class);
    }
    
    public Response saveCategory(Category category){
        return client
            .target(REST_URI_CATEGORY)
            .request(MediaType.APPLICATION_JSON)
            .post(Entity.entity(category, MediaType.APPLICATION_JSON));
    }
    
    public Response updateCategory(Long id,Category category){
        return client
            .target(REST_URI_CATEGORY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .put(Entity.entity(category, MediaType.APPLICATION_JSON));
    }

    public String deleteCategory(Long id){
        return client
            .target(REST_URI_CATEGORY+"/"+id)
            .request(MediaType.APPLICATION_JSON)
            .delete(String.class);
    }
}
