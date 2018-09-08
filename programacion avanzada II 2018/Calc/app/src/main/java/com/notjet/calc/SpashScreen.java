package com.notjet.calc;

import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class SpashScreen extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_spash_screen);
        final Handler handler = new Handler();
        final Intent intent = new Intent(this, MainActivity.class);
        final AppCompatActivity act = this;
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                startActivity(intent);
                act.finish();
            }
        }, 4000);

    }


}
