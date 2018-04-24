page 60h,132h
title pixel
.model small
.stack 64h 


.data ;------------DATOS Y VARIABLES-------------- 


    menu1 db 'LINEA EN ENSAMBLADOR',0ah,0dh,'$' ;variables de texto
    opcion1 db '1) roja ',0ah,0dh,'$'           ;aqui se muestra el menu
    opcion2 db '2) verde ',0ah,0dh,'$'          ;con todas las opciones de colores                     
    opcion3 db '3) azul ',0ah,0dh,'$'
    
    uno db '1','$'      ;estas son variables para
    dos db '2','$'      ;comparar el texto 
    tres db '3','$'
     
    ciclo  db '20','$'  ;esta se la va a utilizar para hacer 20 pixeles seguidos
    
    datos label byte            ;en estas 4 lineas
        maxlon db 30h           ;se recive la opcion
        real db ?               ;para luego ser procesada
        entrada db 31h dup('')  ;
    
     
    
.code ;--------------CODIGO FUENTE----------------- 


    inicio proc far  ;funcion principal o de inicio
        mov ax,@data ;lleva los datos
        mov ds,ax    ;a su registro
        mov es,ax    ;y un registro extra para caracteres
        
        call pantalla ;llama a la funcion pantalla
        call cursor   ;llama a la funcion cursor
        call cadena   ;llama a la funcion cadena
        call entrar   ;llama a la funcion entrar
        call comparar ;llama a la funcion comparar
        
        call pausa    ;llama a la funcion pausa
        
        
        salir:        ;aqui 
        mov ax,4c00h  ;termina
        int 21h       ;el 
        inicio endp   ;programa
    
    
    entrar proc near  ;esta funcion sirve para guardar nuestra opcion
        mov ah,0ah    ;en la variable entrada en otras palabras
        lea dx,datos  ;entramos texto por teclado y lo guardamos en
        int 21h       ;una variable
        ret
    entrar endp
    
    pantalla proc near ;en esta funcion alistamos la pantalla para mostrar texto
        mov ax,0600h
        mov bh,71h
        mov cx,0000h
        mov dx,184fh
        int 10h
        ret
        pantalla endp
    
    cursor proc near   ;en esta funcion alistamos el cursor para mostrar texto
        mov ah,02h
        mov bh,00h
        mov dx,0505h
        int 10h
        ret
        cursor endp
    
    cadena proc near   ;en esta funcion mostramos el texto
        mov ah,09h
        lea dx,menu1   ;texto que esta en menu1 (vease menu1 en datos y variables)
        int 21h 
        lea dx,opcion1 ;texto que esta en opcion1 (vease opcion1 en datos y variables)
        int 21h
        lea dx,opcion2 ;texto que esta en opcion2 (vease opcion2 en datos y variables)
        int 21h
        lea dx,opcion3 ;texto que esta en opcion3 (vease opcion3 en datos y variables)
        int 21h
        ret 
        cadena endp
    
    modogra proc near   ;en esta funcion ponemos al programa en modo grafico
        mov ah,0h
        mov al,13h
        int 10h
        ret
        modogra endp
    
     comparar proc near ;en esta funcion se compara nuestra entrada con las posibles opciones
        
        call modogra    ;llama a la funcion modogra
        lea si,entrada  ;metemos la variable entrada en el registro indice
        mov al,[si]     ;movemos en registro indice a el registro ax en la parte low
        
        
        lea di,uno      ;metemos la vatiable uno (vease uno en datos y variables) en el registro destino
        cmp al,[di]     ;comparamos registro "al" con registro destino "osea 1 con lo que entramos por teclado" 
        je op1          ;si es verdadero vamos a la parte op1 en el programa
        
        lea di,dos      ;metemos la vatiable dos (vease dos en datos y variables) en el registro destino
        cmp al,[di]     ;comparamos registro "al" con registro destino "osea 2 con lo que entramos por teclado"
        je op2          ;si es verdadero vamos a la parte op2 en el programa
        
        lea di,tres     ;metemos la vatiable tres (vease tres en datos y variables) en el registro destino
        cmp al,[di]     ;comparamos registro "al" con registro destino "osea 3 con lo que entramos por teclado"
        je op3          ;si es verdadero vamos a la parte op3 en el programa
        
        jmp salir       ;si ninguna comparacion fue verdadera vamos a la parte salir en el programa(vease salir en la funcion de inicio)
        
        ret
        
    comparar endp
    
    linea proc near    ;funcion linea que nos dibuja una linea en pantalla
        op1:           ;parte op1 en el programa
        mov al,28h     ;mueve a "al" el color que tendra la linea en este caso rojo
        jmp sig        ;incondicionalmente vamos a la parte sig en el programa
        
        op2:           ;parte op2 en el programa
        mov al,78h     ;mueve a "al" el color que tendra la linea en este caso verde
        jmp sig        ;incondicionalmente vamos a la parte sig en el programa
        
        op3:           ;parte op3 en el programa
        mov al,09h     ;mueve a "al" el color que tendra la linea en este caso azul
        jmp sig        ;incondicionalmente vamos a la parte sig en el programa
         
        sig:           ;parte sig en el programa
        
        mov cx,10h     ;empezamos desde el punto 10(hexadecimal) en X
        mov dx,20h     ;empezamos desde el punto 20(hexadecimal) en Y
        mov ah,0ch     ;funcion de dibujado de pixel
        
        mov bl,00h     ;el registro bl lo usamos para nuestro ciclo 
        lea di,ciclo   ;metemos la variable ciclo en el registro destino
            
        lineal:         
                       ;parte linea en el programa
        inc dx         ;inclementamos posicion en Y
        inc cx         ;inclementamos posicion en X                           
        int 10h        ;interrupcion que dibuja pixel 
        inc bl         ;incrementamos el registro bl
        cmp bl,[di]    ;comparamos si el registro bl es igual al registro destino "osea si el numero de pixeles es igual a 20"
        jne lineal      ;si no es asi repetimos el proceso desde la parte linea en el programa
        
        ret 
        linea endp
    
    pausa proc near   ;funcion pausa que nos pausa el programa
        mov ah,00h
        int 16h
        ret
        pausa endp
   
end

        
        
        
        
        
        