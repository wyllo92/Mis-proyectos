@extends('layouts.plantilla')

@section ('title', 'cursos create')

@section('content')
    <h1>aqui puedes crear un curso nuevo</h1>

    <form action="{{route('cursos.store')}}" method="post">

        @csrf

          <label class="form-label" for="form4Example1">
            Name:
            <br>  
          <input type="text" name="name" value="{{old('name')}}">
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
        <input type="text" name="slug" value="{{old('slug')}}">
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
          <textarea name="descripcion" rows="5">{{old('descripcion')}}</textarea>
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
          <input type="text" name="categoria" value="{{old('categoria')}}">
        </label>
        <br>

        @error('categoria')
        <br>
        <span>*{{$message}}</span>
        <br>
          
      @enderror
       
          <button type="submit">enviar formulario</button>
          

      </form>
@endsection


    
