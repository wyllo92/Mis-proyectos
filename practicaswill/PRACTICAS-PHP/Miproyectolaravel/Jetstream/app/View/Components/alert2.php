<?php

namespace App\View\Components;

use Closure;
use Illuminate\Contracts\View\View;
use Illuminate\View\Component;

class alert2 extends Component
{
    public $title;
    public $value;
    public $icon;

    public function __construct($title, $value, $icon)
    {
        $this->title = $title;
        $this->value = $value;
        $this->icon = $icon;
    }

    
    public function render(): View|Closure|string
    {
        return view('components.alert2');
    }
}
