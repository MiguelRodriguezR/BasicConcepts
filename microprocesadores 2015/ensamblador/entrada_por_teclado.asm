; multi-segment executable file template.

; Entrada Por teclado

page 60h,132h
title entrada
.model small
.stack 64h
.data   
    cadena db 'digite nombre : ','$'
    cadena2 db 'digite apellido : ','$' 
    paso1 db '               '  
    paso2 db '               ' 
    
    datos label byte
        maxlon db 20h
        real db ?
        caract db 21h dup('')
    
.code
    inicio proc far
        mov ax,@data
        mov ds,ax
        mov es,ax
        call limpiar
        call cursor
        call mostrar
        call entrar   
        call pasar
        call limpiar
        call cursor
        call mostrar2
        call entrar
        call pasar2 
        call limpiar
        call fin
        call indicar
        
        
        mov ax,4c00h
        int 21h
    inicio endp
    
    pasar proc near
        lea si,caract
        lea di,paso1
        mov bx,0000h
        mov bl,real 
        mov cx,bx
        ciclo2:
            mov al,[si]
            mov [di],al
            inc si
            inc di
            loop ciclo2 
        mov [di],'$'
        ret
    pasar endp 
    
    pasar2 proc near
        lea si,caract
        lea di,paso2
        mov bx,0000h
        mov bl,real 
        mov cx,bx
        ciclo:
            mov al,[si]
            mov [di],al
            inc si
            inc di
            loop ciclo 
        mov [di],'$'
        ret
    pasar2 endp 
    
    limpiar proc near
        mov ax,0600h
        mov bh,30h
        mov cx,0000h
        mov dx,184fh
        int 10h
        ret
    limpiar endp
    
    cursor proc near
        mov ah,02h
        mov dx,0505h
        int 10h
        ret
    cursor endp
    
    mostrar proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,cadena
        int 21h
        ret
    mostrar endp  
    
    mostrar2 proc near 
        mov ax,0000h
        mov ah,09h
        lea dx,cadena2
        int 21h
        ret
    mostrar2 endp
         
    entrar proc near
        mov ah,0ah
        lea dx,datos
        int 21h
        ret
    entrar endp  
    
    fin proc near
        mov bh,00h
        mov bl,real
        mov caract[bx+1h],0AH 
        mov caract[bx+2h],0DH
        mov caract[bx+3h],'$'
        
    fin endp    
             
    
    indicar proc near
        call cursor
        mov ah,09h
        lea dx,paso1
        int 21h  
        lea dx,paso2
        int 21h
    indicar endp
    
    
    
END