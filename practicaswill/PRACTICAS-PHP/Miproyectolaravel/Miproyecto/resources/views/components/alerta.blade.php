<div>
    <!-- It is quality rather than quantity that matters. - Lucius Annaeus Seneca -->

    <h2> este es mi nuevo componente</h2>
    <h1> el tipo de error es: {{$type}}</h1>
    <h1> este es el mensaje: {{$mensaje}}</h1>

    @foreach ($lenguajes('c#') as $item)

        <h4>{{$item}}</h4>
        
    @endforeach
</div>