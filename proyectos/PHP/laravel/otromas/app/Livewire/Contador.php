<?php

namespace App\Livewire;

use Livewire\Component;

class Contador extends Component
{
    public $count=0;

    public function decrement($cant){
        $this->count -=$cant;
    }

    public function increment($cant){
        $this->count +=$cant;
    }

    public function render()
    {
        return view('livewire.contador');
    }
}
