<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StoreCurso extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'name' => ['required', 'min:3'],
            'slug'=>['required', 'unique:cursos'],
            'descripcion' => 'required',
            'categoria' => 'required',
        ];
    }

    public function messages(): array
    {
        return[

            'descripcion.required'=> 'la descripcion es obligatoria'

        ];
    }

    public function attributes(): array
    {
        return[

            'name'=>'nombre del curso',
        ];
    }
    
}
