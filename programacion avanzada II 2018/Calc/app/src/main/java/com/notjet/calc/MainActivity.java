package com.notjet.calc;


import android.content.res.Configuration;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;





public class MainActivity extends AppCompatActivity {


    public String expresion;
    public TextView screen;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        expresion = "";
        checkOrientation();




    }

    public void checkOrientation(){
        if(getResources().getConfiguration().orientation == Configuration.ORIENTATION_PORTRAIT)
        {
            screen = findViewById(R.id.textViewScreen2);
        } else {
            screen = findViewById(R.id.textViewScreen);
        }
    }

    public void setExpresion(View view){
       Button b = (Button) view;
       String retText;
       retText = b.getText().toString();

       switch (retText){
           case "x!":
               retText = "!";
               break;

           case "sin":
               retText = "sin(";
               break;

       }

       expresion += retText;
       screen.setText(expresion);
       //Log.d("e",""+getResources().getConfiguration().orientation);
    }



}
