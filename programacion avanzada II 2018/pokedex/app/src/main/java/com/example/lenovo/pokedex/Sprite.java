package com.example.lenovo.pokedex;

import com.google.gson.annotations.SerializedName;

public class Sprite {

    @SerializedName("back_default")
    private String back;

    @SerializedName("front_default")
    private String front;

    Sprite(){}

    public String getBack() {
        return back;
    }

    public void setBack(String back) {
        this.back = back;
    }

    public String getFront() {
        return front;
    }

    public void setFront(String front) {
        this.front = front;
    }
}
