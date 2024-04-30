<div>

<form class="mb-4" wire:submit="save">


    <x-input 
    wire:model="pais"
    placeholder="agregue un pais"/>

    <x-button >agregar</x-button>


</form>

   <ul class="list-disc list-inside space-y-2">

    @foreach ($paises as $index => $pais)

        <li wire:key="pais-{{$index}}">
            
            <span wire:mouseenter="changeActive('{{$pais}}')">
                {{$index}} {{ $pais }}
            </span>

            <x-danger-button wire:click="delete({{$index}})">
                x              
            </x-danger-button>
        </li>

    @endforeach
   </ul>

   {{$active}}
   

   