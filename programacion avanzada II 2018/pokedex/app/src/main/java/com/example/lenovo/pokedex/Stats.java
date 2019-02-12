package com.example.lenovo.pokedex;

import com.google.gson.annotations.SerializedName;

class Stats {

    @SerializedName("base_stat")
    private Integer base;

    Stats(){}

    public Integer getBase() {
        return base;
    }

    public void setBase(Integer base) {
        this.base = base;
    }

}
