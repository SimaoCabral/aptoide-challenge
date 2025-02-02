package com.android.support.exercise.bd

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.android.support.exercise.bd.dao.UserDao
import com.android.support.exercise.bd.entities.User

@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao

    companion object {

        fun getDatabase(context: Context): AppDatabase {
            val app =  Room.databaseBuilder(context, AppDatabase::class.java, "user-database")
                .build()
            if (app.userDao().getUserCount() == 0){
                app.userDao().insertUser(
                    User(
                        1,
                        "John Doe",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Barack_Obama_profile.jpg/446px-Barack_Obama_profile.jpg"
                    )
                )
            }
            return app
        }
    }
}