<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
            {{ __('Dashboard') }}
        </h2>
    </x-slot>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            {{--@livewire('create-post', [
                'title'=>'hola mundo desde la vista del dashboard',
                'user'=>1,
            ])

            @livewire('Paises')--}}
            <x-mio>
                <x-slot:title>
                    william page
                </x-slot>

                contenido principal
            </x-mio>
        </div>
    </div>
</x-app-layout>
