; Agenda simple ensamblador Miguel Angel Rodriguez

page 60h,132h
title AGENDA
.model small
.stack 64h
.data
    opcion1 db '1) Nombre ',0ah,0dh,'$'
    opcion2 db '2) Telefono ',0ah,0dh,'$'
    opcion3 db '3) Direccion ',0ah,0dh,'$' 
    opcion4 db '4) Mostrar ',0ah,0dh,'$' 
    opcion5 db '5) Salir ',0ah,0dh,'$'
    peticion db 'Digite su opcion : ','$' 
    peticion2 db 'Digite su nombre : ','$'
    peticion3 db 'Digite su telefono : ','$'
    peticion4 db 'Digite su direccion : ','$'
    uno db '1','$'
    dos db '2','$'
    tres db '3','$'
    cuatro db '4','$' 
    cinco db '5','$'
    nombre db '               $'  
    telefono db '              $'
    direccion db '              $'
    salto db 0ah,0dh
    dol db '$'
    
    datos label byte
        maxlon db 30h
        real db ?
        entrada db 31h dup('')
        
.code
    inicio proc far
        mov ax,@data
        mov ds,ax
        mov es,ax
        
        nuevo:
        call limpiar
        ;call cursor
        ;call formatear
        call mostrar
        call entrar 
        call comparar
        jmp salir
        
        op1:
        call limpiar
        call cursor
        call mostrarn
        call entrar
        call pasarn
        jmp nuevo
        
        op2:
        call limpiar
        call cursor
        call mostrart
        call entrar
        call pasart 
        jmp nuevo
        
        op3:
        call limpiar
        call cursor
        call mostrard
        call entrar
        call pasard
        jmp nuevo
        
        op4:
        call limpiar
        call cursor
        call mostrardatos  
        jmp nuevo
        
        
        salir:
        mov ax,4c00h
        int 21h
    inicio endp
    
    formatear proc near
        mov ax,0600h
        mov bh,30h
        mov cx,0000h
        mov dx,184fh
        int 10h
        ret
    formatear endp
    
    limpiar proc near  
        mov ah,00h ;limpia la pantalla
		mov al,03h
		int 10h
        ret
    limpiar endp
    
    cursor proc near
        mov ah,02h
        mov dx,0505h
        int 10h
        ret
    cursor endp 
    
    mostrardatos proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,nombre
        int 21h 
        lea dx,salto
        int 21h
        lea dx,telefono
        int 21h  
        lea dx,salto
        int 21h
        lea dx,direccion 
        int 21h 
        lea dx,salto
        int 21h
        mov ah,00h
        int 16h
        
        ret
    mostrardatos endp
    
    mostrar proc near 
        mov ax,0000h
        mov ah,09h 
        lea dx,salto
        int 21h
        lea dx,opcion1
        int 21h 
        lea dx,opcion2
        int 21h
        lea dx,opcion3
        int 21h  
        lea dx,opcion4
        int 21h
        lea dx,opcion5
        int 21h
        lea dx,peticion
        int 21h 
        
        ret
    mostrar endp
    
    mostrarn proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,peticion2
        int 21h 
        
        ret
    mostrarn endp 
    
    mostrart proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,peticion3
        int 21h 
        
        ret
    mostrart endp  
    
    mostrard proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,peticion4
        int 21h 
        
        ret
    mostrard endp
    
    entrar proc near
        mov ah,0ah
        lea dx,datos
        int 21h
        ret
    entrar endp 
    
    comparar proc near
        lea si,entrada
        mov al,[si]
        
        lea di,uno
        cmp al,[di]
        je op1 
        
        lea di,dos
        cmp al,[di]
        je op2
        
        lea di,tres
        cmp al,[di]
        je op3 
        
        lea di,cuatro
        cmp al,[di]
        je op4  
        
        lea di,cinco
        cmp al,[di]
        je salir
        
        ret
        
    comparar endp
    
    
    pasarn proc near
        lea si,entrada
        lea di,nombre
        mov bx,0000h
        mov bl,real 
        mov cx,bx
        ciclon:
            mov al,[si]
            mov [di],al
            inc si
            inc di
            loop ciclon 
        mov [di],'$'
        ret
    pasarn endp 
    
    pasart proc near
        lea si,entrada
        lea di,telefono
        mov bx,0000h
        mov bl,real 
        mov cx,bx
        ciclot:
            mov al,[si]
            mov [di],al
            inc si
            inc di
            loop ciclot 
        mov [di],'$'
        ret
    pasart endp 
    
    pasard proc near
        lea si,entrada
        lea di,direccion
        mov bx,0000h
        mov bl,real 
        mov cx,bx
        ciclod:
            mov al,[si]
            mov [di],al
            inc si
            inc di
            loop ciclod 
        mov [di],'$'
        ret
    pasard endp
END
                    
                    