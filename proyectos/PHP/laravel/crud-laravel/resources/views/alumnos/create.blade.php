@extends('layouts/templade')

@section('title', 'registrar alumno|escuela')

@section('contenido')

    <main>
        <div class="container py-4">
            <h2>resgistrar alumno</h2>

            @if (errors->any())
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    <strong>Holy guacamole!</strong> You should check in on some of those fields below.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            @endif
            
            <form action="{{ url('alumnos') }}" method="POST">
                @csrf
                <div class="mb-3 row">
                    <label for="matricula" class="col-sm-2 col-form-label">matricula</label>
                    <div class="col-sm-5">
                        <input type="text" name="matricula" id="matricula" value="{{ old('matricula') }}"
                            placeholder="matricula" required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="nombre" class="col-sm-2 col-form-label">nombre completo:</label>
                    <div class="col-sm-5">
                        <input type="text" name="nombre" id="nombre" value="{{ old('nombre') }}" placeholder="nombre"
                            required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="fecha" class="col-sm-2 col-form-label">fecha de nacimiento</label>
                    <div class="col-sm-5">
                        <input type="date" name="fecha" id="fecha" value="{{ old('fecha') }}"
                            placeholder="fecha de nacimiento" required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="telefono" class="col-sm-2 col-form-label">telefono</label>
                    <div class="col-sm-5">
                        <input type="text" name="telefono" id="telefono" value="{{ old('telefono') }}"
                            placeholder="telefono" required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="email" class="col-sm-2 col-form-label">email</label>
                    <div class="col-sm-5">
                        <input type="text" name="email" id="email" value="{{ old('email') }}" placeholder="email">
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="nivel" class="col-sm-2 col-form-label">nivel:</label>
                    <div class="col-sm-5">
                        <select name="nivel" id="nivel" class="form-select" required>
                            <option value="">seleccionar nivel</option>
                            @foreach ($niveles as $nivel)
                                <option value="{{ $nivel->id }}">{{ $nivel->nombre }}</option>
                            @endforeach
                        </select>
                    </div>
                </div>
                <a href="{{ url('alumnos') }}" class="btn btn-secondary">regresar</a>
                <button type="submit" class="btn btn-success">guardar</button>
            </form>
        </div>
    </main>
