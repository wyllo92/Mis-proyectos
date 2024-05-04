@props(['cursos'])

<ul>
    @foreach ($cursos as $curso)

    <li>
        <a href="{{route('cursos.show', $curso)}}">{{ $curso->name}}</a>
    </li>
        
    @endforeach

</ul>