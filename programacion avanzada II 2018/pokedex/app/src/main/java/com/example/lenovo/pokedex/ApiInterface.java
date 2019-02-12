package com.example.lenovo.pokedex;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface ApiInterface {

    @GET("api/v2/pokemon/{id}")
    Call<Pokemon> getPokemon(@Path("id") int id);

    @GET("{resource_uri}")
    Call<Sprite> getSprite(@Path("resource_uri") String resourceUri);
}
