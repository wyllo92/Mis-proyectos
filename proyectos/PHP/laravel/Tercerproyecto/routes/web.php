<?php

use App\Http\Controllers\PostController;
use Illuminate\Support\Facades\Route;



Route::view('/', 'welcome' )->name('home');
Route::view('/contact', 'contact')->name('contact');
Route::get('/blog', [PostController::class, 'index'])->name('posts.index');

Route::get('/blog/create', [PostController::class, 'create'])->name('posts.create');

Route::POST('/blog', [PostController::class, 'store'])->name('posts.store');

Route::get('/blog/{post}', [PostController::class, 'show'])->name('posts.show');

Route::get('/blog/{post}/edit', [PostController::class, 'edit'])->name('posts.edit');

Route::patch('/blog/{post}', [PostController::class, 'update'])->name('posts.update');

Route::delete('/blog/{post}', [PostController::class, 'destroy'])->name('posts.destroy');


/*route::resource('blog', PostController::class, [

    'names' => 'posts',
    'parameters' => ['blog' => 'posts']
]);*/

Route::view('/about', 'about')->name('about');