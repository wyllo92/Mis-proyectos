<?php


use App\Http\Controllers\Admin\AdministratorController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Admin\InvoiceController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;
use SebastianBergmann\CodeCoverage\Report\Html\Dashboard;


//route::view('/' , 'welcome');//
route::view('/' , 'layouts.app');

Route::get('/inicio', [UserController::class, 'index']);

Route::get('/nombre/{name}', [UserController::class, 'showname']);

Route::get('/suma/{num?}', [UserController::class, 'suma']);

route::namespace('Admin')->group(function(){

    Route::get('Admin', [AdministratorController::class, 'index']);
    Route::get('Dashboard', [DashboardController::class, 'index']);
    Route::get('Invoice', [InvoiceController::class, 'index']);
});

