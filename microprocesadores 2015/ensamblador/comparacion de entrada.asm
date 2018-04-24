; multi-segment executable file template.

page 60h,132h
title comparacion
.model small
.stack 64h
.data
     datos label byte
        maxlon db 2h
        real db ?
        caract db 3h dup ('')
        mensaje db 'digite opcion : ','$'
        uno db '1','$'
        letrero1 db 'CORRECTISIMO','$'
        letrero2 db 'ERROR JOVEN','$'
.code
    inicio proc far
        mov ax,@data
        mov ds,ax
        mov es,ax
        call limpiar
        call cursor
        call mostrar
        call entrar
        lea si,caract
        lea di,uno
        mov al,[si]
        cmp al,[di]
        jne a1
        call centrar1
        jmp a2
     a1:call centrar2
     a2:mov ax,4c00h
        int 21h
    inicio endp 
    
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
        mov ah,09h
        lea dx,mensaje
        int 21h
        ret
    mostrar endp
    
    entrar proc near
        mov ah,0ah
        lea dx,datos
        int 21h
        ret
    entrar endp 
    
    centrar1 proc near
        mov ah,09h
        lea dx,letrero1
        int 21h
        ret
    centrar1 endp
    
    centrar2 proc near
        mov ah,09h
        lea dx,letrero2
        int 21h
        ret
    centrar2 endp
    
    
    
    
    
      
         