package com.example.lenovo.pokedex;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class DetailActivity extends AppCompatActivity {

    private TextView tvName, tvTypes, tvAttack, tvDefense, tvSpeed;
    private ImageView ivPokemon;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        tvName =  findViewById(R.id.tv_detail_name);
        tvTypes =  findViewById(R.id.tv_detail_types);
        tvAttack =  findViewById(R.id.tv_detail_attack);
        tvDefense =  findViewById(R.id.tv_detail_defense);
        tvSpeed =  findViewById(R.id.tv_detail_speed);
        ivPokemon =  findViewById(R.id.iv_detail_pokemon);

        Intent i = getIntent();
        Toast.makeText(DetailActivity.this, i.getIntExtra("ID", 0) + "", Toast.LENGTH_SHORT).show();

        int id = i.getIntExtra("ID", 0);
        requestData(id);
    }

    private void requestData(int id) {
        final ApiInterface apiService = ApiClient.getClient().create(ApiInterface.class);

        Call<Pokemon> call = apiService.getPokemon(id);
        call.enqueue(new Callback<Pokemon>() {
            @Override
            public void onResponse(Call<Pokemon> call, Response<Pokemon> response) {
                Pokemon pokemon;

                if(response.isSuccessful()) {
                    pokemon = response.body();
                    String orden = "";
                    for(int x = 0; x<Integer.parseInt(pokemon.getHeight())/2; x++){
                        orden += Character.toString((char)9734);
                    }
                    tvName.setText(pokemon.getName());
                    tvTypes.setText(pokemon.pokeTypesToString());
                    tvAttack.setText("ALTURA: "+pokemon.getHeight()+"m");
                    tvDefense.setText("PESO: "+pokemon.getWeight()+"kg");
                    tvSpeed.setText("PODER: "+ orden);
                    Picasso.with(ivPokemon.getContext())
                            .load(pokemon.getSprite().getFront())
                            .resize(228,228)
                            .into(ivPokemon);

                }
            }

            @Override
            public void onFailure(Call<Pokemon> call, Throwable t) {

            }
        });
    }
}
