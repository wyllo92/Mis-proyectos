@vite('resources/css/app.css')

<article {{$attributes}} class=" border-l-4 {{$clases}}  p-4" role="alert">
    <h1 class="font-bold">{{$title}}</h1>
    {{$slot}}
  </article>