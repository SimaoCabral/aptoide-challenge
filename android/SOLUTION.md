# Issue Solving

The following intends to explain the issues identified in the codebase, that did not allow the execution of the application. The code were altered without majorly changing the created execution flow.

## Database Access

**User Entity**

To properly work with Room database, the Entity class needed to be constructed accordingly with the [specifications](https://developer.android.com/training/data-storage/room/defining-data). In this case the Primary Key Annotation was missing and was added accordingly with `@PrimaryKey val id: Int`.

**Datase Access**

In the way that the method `loadUserData(context: Context)` from the `MainActivityViewModel`, there is an attempt to consult the repository in the Main Thread that should remain free for the UI. Similar to what was done in the `loadPostsData()` we should launch an async operation by using Coroutines, with the threads dealing with IO operations and only switch the CoroutineScope back to the Main threads, when affecting hte UI State, as seen below.

```kotlin
fun loadUserData(context: Context) {
        CoroutineScope(Dispatchers.IO).launch {
            try {
                AppDatabase.getDatabase(context)
                    ?.userDao()
                    ?.getAllUsers()?.firstOrNull()?.let {
                        withContext(Dispatchers.Main){
                            _userName.value = it.name
                            _userImage.value = it.image
                        }
                    }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
```

## Remote requests

To be able to use Glide and Retrofit the app needs permissions to use the internet to make the requests. To solve it we need to define
the permission in the manifest by inserting

```
<uses-permission android:name="android.permission.INTERNET"/>
```

## Main activity

The methods that created the activity were out of order, the layout of the whole view would need to be set before affecting the elements belonging to the view.

After calling the `setContentView(R.layout.activity_main)` before the doing the `findById()` operations, that issue was corrected.


## Posts Adapter

The `getItemCount()` method was not returing the updated value of the size of the lists. With the return set to 0 it assumes always assumes that there are no items to present, even if the list is updated. By returning the size of the list, the adapter starts working accordingly.
