<?php

namespace App\Http\Controllers;

use App\Models\Nivel;
use App\Models\Alumno;
use Illuminate\Http\Request;

class AlumnoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return view('alumnos.index');
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        
        return view('alumnos.create', ['niveles'=>Nivel::all()]);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $request->validate([
            'matricula' => 'required|unique:alumnos|max:10',
            'nombre'=> 'required|max:255',
            'fecha_nacimiento'=> 'required|date',
            'telefono'=> 'required|',
            'email'=> 'nullable|email',
            'nivel'=> 'required'
        ]);
    }

    /**
     * Display the specified resource.
     */
    public function show(Alumno $alumno)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Alumno $alumno)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Alumno $alumno)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Alumno $alumno)
    {
        //
    }
}
