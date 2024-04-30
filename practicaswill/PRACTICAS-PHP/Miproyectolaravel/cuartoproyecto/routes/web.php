<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\CursoController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

/*Route::get('/', function () {
    return view('welcome');
});*/

route::get('/', HomeController::class, '__invoke')->name('home');

route::view('nosotros', 'nosotros')->name('nosotros');

route::resource('cursos', CursoController::class);



route::get('cursos', [CursoController::class, 'index'])->name('cursos.index');

route::get('cursos/create', [CursoController::class, 'create'])->name('cursos.create');

route::post('cursos', [CursoController::class, 'store'])->name('cursos.store');

route::get('cursos/{curso}', [CursoController::class, 'show'])->name('cursos.show');

route::get('cursos/{curso}/edit', [CursoController::class, 'edit'])->name('cursos.edit');

route::put('cursos/{curso}', [CursoController::class, 'update'])->name('cursos.update');

route::delete('cursos/{curso}', [CursoController::class, 'destroy'])->name('cursos.destroy');


/*route::controller(CursoController::class)->group(function(){

    route::get('/cursos', 'index');
    route::get('/cursos/create', 'create');
    route::get('/cursos/{curso}', 'show');

});*/