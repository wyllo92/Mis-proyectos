<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            {{ __('coders training') }}
        </h2>
    </x-slot>

    <div class="py-12" id="alerta" class="mb-4" role="prueba">
        <x-alert2 title="Total Users" value="500" icon="fas fa-users" />
        <x-alert2 title="Revenue" value="$10,000" icon="fas fa-dollar-sign" />

    </div>
</x-app-layout>
