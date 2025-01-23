package com.android.support.exercise.bd.entities

import androidx.room.Entity

@Entity
data class User(
    val id: Int,
    val name: String,
    val image: String
)

