<?php

namespace App\Livewire;

use Livewire\Component;

class Paises extends Component
{
    public $paises = [
        'peru',
        'colombia',
        'argentina'
    ];

    public $pais;
    public $active;

    public function save(){

        array_push($this->paises, $this->pais);
        $this->pais='';

    }

    public function delete($index){

        unset($this->paises[$index]);

    }

    public function changeActive($pais){

        $this->active=$pais;

    }
    
    public function render()
    {
        return view('livewire.paises');
    }
}
