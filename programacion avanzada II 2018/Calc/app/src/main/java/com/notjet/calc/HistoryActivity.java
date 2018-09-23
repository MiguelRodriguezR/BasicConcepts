package com.notjet.calc;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class HistoryActivity extends AppCompatActivity {

    public TextView historyTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);
        historyTextView = findViewById(R.id.historyTextView);
        readFile();


    }

    public void readFile(){

        String result = "History: \n";
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
            result += sb.toString();
        }catch (Exception e){}


        historyTextView.setText(result);
    }
}
