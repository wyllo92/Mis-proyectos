@extends('layouts.plantilla')

@section ('title', ' cursos value="{{$curso->name}}"edit')

@section('content')
    <h1>aqui puedes editar este curso</h1>

    <form action="{{route('cursos.update', $curso)}}" method="post">

        @csrf

        @method("put")
        
          <label class="form-label" for="form4Example1">
            Name:
            <br>  
          <input type="text" name="name" value="{{old('name', $curso->name)}}">
        </label>
        <br>
       
        @error('name')
        <br>
        <span>*{{$message}}</span>
        <br>
          
      @enderror

      <label class="form-label" for="form4Example1">
        slug:
        <br>  
      <input type="text" name="slug" value="{{old('slug', $curso->slug)}}">
    </label>
    <br>
   
    @error('slug')
      <br>
      <span>*{{$message}}</span>
      <br>

    @enderror
       
          <label class="form-label" for="form4Example2">
            Descripcion:
            <br>
          <textarea name="descripcion" rows="5">{{old('descripcion', $curso->descripcion)}}</textarea>
        </label>
        <br>

        @error('descripcion')
        <br>
        <span>*{{$message}}</span>
        <br>
          
      @enderror
      
       
          <label class="form-label" for="form4Example3">
            Categoria:
            <br>
          <input type="text" name="categoria" value="{{old('categoria', $curso->categoria)}}">
        </label>
        <br>

        @error('categoria')
        <br>
        <span>*{{$message}}</span>
        <br>
          
      @enderror

        
       
          <button type="submit">actualizar formulario</button>
          

      </form>
@endsection


    