package com.notjet.calc;


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;





public class MainActivity extends AppCompatActivity {



    public TextView screen;
    public String operator;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        screen = findViewById(R.id.textView);
        operator = "";
        eraseAll();
        setListeners();
    }

    void setListeners(){

        final Button button2 = findViewById(R.id.button2);
        final Button button5 = findViewById(R.id.button5);
        final Button button6 = findViewById(R.id.button6);
        final Button button7 = findViewById(R.id.button7);
        final Button button9 = findViewById(R.id.button9);
        final Button button10 = findViewById(R.id.button10);
        final Button button11 = findViewById(R.id.button11);
        final Button button12 = findViewById(R.id.button12);
        final Button button13 = findViewById(R.id.button13);
        final Button button14 = findViewById(R.id.button14);
        final Button button15 = findViewById(R.id.button15);
        final Button button16 = findViewById(R.id.button16);
        final Button button19 = findViewById(R.id.button19);
        final Button button20 = findViewById(R.id.button20);
        final Button button21 = findViewById(R.id.button21);
        final Button button22 = findViewById(R.id.button22);

        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
               updateScreenText(button2.getText().toString());
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                checkOperator();
                if(operator=="" && screen.getText().toString()!="" ) {
                    operator = "*";
                    updateScreenText(" " + button5.getText().toString() + " ");
                }
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button6.getText().toString());
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button7.getText().toString());
            }
        });
        button9.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button9.getText().toString());
            }
        });
        button10.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button10.getText().toString());
            }
        });
        button11.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button11.getText().toString());
            }
        });
        button12.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                checkOperator();
                if(operator=="" && screen.getText().toString()!=""){
                    operator = "/";
                    updateScreenText(" "+button12.getText().toString()+" ");
                }

            }
        });
        button13.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button13.getText().toString());
            }
        });
        button14.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button14.getText().toString());
            }
        });
        button15.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button15.getText().toString());
            }
        });
        button16.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                checkOperator();
                if(operator=="" && screen.getText().toString()!=""){
                    operator = "-";
                    updateScreenText(" "+button16.getText().toString()+" ");
                }
            }
        });
        button19.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                checkOperator();
                if(operator=="" && screen.getText().toString()!="") {
                    operator = "+";
                    updateScreenText(" " + button19.getText().toString() + " ");
                }
            }
        });
        button20.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                updateScreenText(button20.getText().toString());
            }
        });
        button21.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                eraseAll();
            }
        });
        button22.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                setTotal();

            }
        });
    }

    void updateScreenText(String e){
        String finalText = screen.getText().toString();
        finalText+=e;
        screen.setText(finalText);
    }



    void setTotal(){
        String[] finalText = screen.getText().toString().split(" ");
        if (finalText.length!=3){
            return;
        }
        float n1 = Float.parseFloat(finalText[0]);
        float n2 = Float.parseFloat(finalText[2]);
        if(operator=="+"){
            float res = n1+n2;
            screen.setText(res+"");
        }
        if(operator=="*"){
            float res = n1*n2;
            screen.setText(res+"");
        }
        if(operator=="/"){
            float res = n1/n2;
            screen.setText(res+"");
        }
        if(operator=="-"){
            float res = n1-n2;
            screen.setText(res+"");
        }
        operator ="";

    }

    void eraseAll(){
        screen.setText("");
        operator ="";
    }

    void checkOperator(){
        if(operator!=""){
            setTotal();
        }
    }
}
