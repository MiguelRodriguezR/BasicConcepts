package com.example.lenovo.pokedex;

import com.google.gson.annotations.SerializedName;

public class PokeType {

    @SerializedName("type")
    private Type type;

    @SerializedName("slot")
    private String slot;

    public PokeType(Type type) {
        this.type = type;
    }


    public Type getType() {
        return type;
    }

    public String getStringType() {
        return type.getName();
    }

    public void setType(Type type) {
        this.type = type;
    }
}

class Type{

    @SerializedName("name")
    private String name;

    public Type(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}