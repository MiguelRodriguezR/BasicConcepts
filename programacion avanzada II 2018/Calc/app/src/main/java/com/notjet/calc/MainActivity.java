package com.notjet.calc;


import android.content.Context;
import android.content.Intent;
import android.content.res.Configuration;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;


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

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {
            case R.id.about:
                setAbout();
                return true;
            case R.id.history:
                setHistory();
                return true;
            default:
                return super.onOptionsItemSelected(item);
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

           case "cos":
               retText = "cos(";
               break;

           case "tan":
               retText = "tan(";
               break;

           case "√":
               retText = "√(";
               break;

           case "ln":
               retText = "ln(";
               break;

           case "log":
               retText = "log(";
               break;

           case "1/x":
               retText = "x1÷";
               break;

           case "e^x":
               retText = "e^(";
               break;

           case "x^2":
               retText = "^2";
               break;

           case "y^x":
               retText = "^";
               break;


       }



       expresion += retText;
       screen.setText(expresion);
       //Log.d("e",""+getResources().getConfiguration().orientation);
    }

    public void deleteAll(View view){
        screen.setText("");
        expresion = "";
    }


    public void setAbout(){
        Intent intent = new Intent(this, About.class);
        startActivity(intent);

    }

    public void setHistory(){
        Intent intent = new Intent(this, HistoryActivity.class);
        startActivity(intent);

    }

    public String readFile(){

        String result = "";
        String FILENAME = "calc_file";
        byte[] bs = new byte[1000];
        FileInputStream is;
        try {

            is= this.getApplicationContext().openFileInput(FILENAME);
            StringBuilder sb = new StringBuilder();
            try {
                BufferedReader reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                String line = null;
                while ((line = reader.readLine()) != null) {
                    sb.append(line).append("\n");
                }
                is.close();
            } catch(OutOfMemoryError om) {
                om.printStackTrace();
            } catch(Exception ex) {
                ex.printStackTrace();
            }
            result = sb.toString();
        }catch (Exception e){}


        return result;
    }

    public void saveResult(View v){
        String FILENAME = "calc_file";
        String string = readFile()+"\n"+screen.getText().toString();


        try {
            FileOutputStream fos = this.getApplicationContext().openFileOutput(FILENAME, Context.MODE_PRIVATE);
            fos.write(string.getBytes());
            fos.close();
        }catch (Exception e){}

    }



}
