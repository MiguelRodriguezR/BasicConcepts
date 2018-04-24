PAGE 60, 132
TITLE Integrantes:[Monica Marcela Aza, Fausto Jojoa Ortiz]
.MODEL SMALL
.STACK 64
.DATA  
;________________________     
;son los msj que se muestran en pantalla   

MENU db 0dh,0ah,'                  UNIVERSIDAD DE NARIÑO  ',0dh,
     db 0dh,0ah,'                 SISTEMAS COMPUTACIONALES ',0dh,0ah,0dh,0ah,
     db 0dh,0ah,'              ****** DATOS PERSONALES ******',0dh,0ah,0dh,0ah,
     db '       1._ [Nombre]',0dh,0ah,
     db '       2._ [Direccion]',0dh,0ah,
     db '       3._ [Telefono]',0dh,0ah,
     db '       4._ [Mostrar]',0dh,0ah, 
     db '       5._ [Salir]',0dh,0ah,0dh,0ah,
     db '       Digite una opcion -->'," $"  

;________________________
;para ingreso de telefono

PHON LABEL BYTE
MAXLONT DB 11
REALT DB ?
PHONE DB 12 DUP(' ') 

;_________________________
;Para ingreso de Direccion 
ADRESS LABEL BYTE
MAXCCION DB 15
REALD DB ?           
DGUARDAR DB 16 DUP('  ')

;______________________ 
;Para ingreso de nombre
INDOMBRE LABEL BYTE   
MAXLONE DB 20   
REALN DB ?
GUARNOM DB 21 DUP( '  ')               
;______________________ 
;Para ingreso de opcion
OPC LABEL BYTE
MAXLONO DB 2
REALO DB ?  
OPCION DB 3 DUP(' ') 

;_________________________ 
;muestra ingreso de opcion
     
     
DNOMBRE DB '  Digite Nombre: ',"$"
DTELEFONO DB ' Digite Telefono: ',"$" 
DIGDIRECCION DB ' Digite Direccion: ',"$" 
DMOSTRAR DB ' Mostrar ',"$"      
ERROR DB ' ERROR <Opcion NO valida>',"$"
DSALIR DB ' Salir',"$" 
DATOS DB '          ****** DATOS INGRESADOS ******',"$"
NOMBRE DB 'NOMBRE: ',"$"
DIRECCION DB 'DIRECCION: ',"$"
TELEFONO DB 'TELEFONO: ',"$"

;____________________________________
;son etiquetas con las que se compara
UNO DB "1",'$'
DOS DB "2" ,'$'
TRES DB "3" ,'$'
CUATRO DB "4",'$'
CINCO DB "5" ,'$'  
                               
.CODE

INICIO PROC FAR
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX     
    CALL LIMPIAR
    CALL CURSOR
    call inicioMenu 
    call fin
    call salir
    
LIMPIAR PROC NEAR 
    MOV AX, 0600H
    MOV BH, 37H
    MOV CX, 0000
    MOV DX, 184FH
    INT 10H
    RET
    LIMPIAR ENDP    

CURSOR PROC NEAR
    MOV AH, 02H ;funcion
    mov dx, 0505
    mov bh,00
    INT 10H
    RET
    CURSOR ENDP

CURSOR1 PROC NEAR
    MOV AH, 02H ;funcion
    mov bh,00
    INT 10H
    RET
    CURSOR1 ENDP

MOSTRARMENU PROC NEAR
    MOV AH, 09H    
    LEA DX, MENU
    INT 21H
    RET
    MOSTRARMENU ENDP   

ENTRAROP PROC NEAR
    MOV AH, 0AH
    LEA DX, OPC
    INT 21H
    RET
    ENTRAROP ENDP  


MOSNOM PROC NEAR
    MOV AH, 09H 
    LEA DX, DNOMBRE
    INT 21H
    RET
    MOSNOM ENDP 


ENTRARNOM PROC NEAR
    MOV AH, 0AH
    LEA DX, INDOMBRE
    INT 21H
    RET
    ENTRARNOM ENDP

FINOM PROC NEAR
    MOV BH, 00
    MOV BL, REALN
    MOV GUARNOM(BX+1),"$"
    RET
    FINOM ENDP 


INDICARNOMBRE PROC NEAR
   mov dx, 0410h
   CALL CURSOR1
   MOV AH, 09H  
   LEA DX, GUARNOM
   INT 21H    
   RET                
   INDICARNOMBRE ENDP


MOSDIR PROC NEAR
    MOV AH, 09H
    LEA DX, DIGDIRECCION
    INT 21H
    RET
    MOSDIR ENDP 


ENTRARDIR PROC NEAR
    MOV AH, 0AH
    LEA DX, ADRESS
    INT 21H
    RET
    ENTRARDIR ENDP 

FINDIR PROC NEAR
    MOV BH, 00
    MOV BL,REALD
    MOV DGUARDAR(BX+1),"$"
    RET
    FINDIR ENDP


INDICARDIRECCION PROC NEAR
   
   MOV DX,0610h
   CALL CURSOR1
   MOV AH, 09H  
   LEA DX,DGUARDAR 
   INT 21H    
   RET
   INDICARDIRECCION ENDP


MOSTELF PROC NEAR
    MOV AH, 09H
    LEA DX, DTELEFONO
    INT 21H
    RET
    MOSTELF ENDP 


ENTRARTEL PROC NEAR
    MOV AH, 0AH
    LEA DX, PHON
    INT 21H
    RET
    ENTRARTEL ENDP 

FINTEL PROC NEAR
    MOV BH, 00
    MOV BL, REALT
    MOV PHONE(BX+1),'$'
    RET
    FINTEL ENDP

INDICARTELEFONO PROC NEAR
   mov dx, 0810H
   CALL CURSOR1
   MOV AH, 09H
   LEA DX, phone  
   INT 21H   
   RET
   INDICARTELEFONO ENDP  


MOSTRARERROR PROC NEAR 
    MOV AH,09H
    LEA DX, ERROR
    INT 21H
    
    MOSTRARERROR ENDP 

 
FIN PROC NEAR
    MOV BH, 00
    MOV BL, REALO
    MOV OPCION(BX+1),"$"
    RET
    FIN ENDP

CDATOS PROC NEAR
    MOV AH,09H
    LEA DX, DATOS
    INT 21H
    RET
    CDATOS ENDP 

CNOMBRE PROC NEAR
    MOV AH,09H
    LEA DX, NOMBRE
    INT 21H
    RET
    CNOMBRE ENDP 

CDIRECCION PROC NEAR
    MOV AH,09H
    LEA DX, DIRECCION
    INT 21H
    RET
    CDIRECCION ENDP

CTELEFONO PROC NEAR
    MOV AH,09
    LEA DX, TELEFONO
    INT 21H
    RET
    CTELEFONO ENDP
    

PAUSA PROC near
   mov ah,00
   int 16h  
   RET
   PAUSA endp 

SALIR PROC NEAR
    MOV Ax, 4c00h
    INT 21H
    SALIR ENDP
    
   
inicioMenu proc near
    
    CALL MOSTRARMENU
    CALL ENTRAROP 
        
    ;______________
    ;Comparacion si la opc ing es 1
    LEA SI,OPCION
    LEA DI, UNO
    MOV AL,[SI]
    CMP AL,[DI]
    JE NOM; etiqueta de nombre
    ;____________                  
    ;Comparacion si la opc ing es 2
    LEA DI, DOS                    
    CMP AL,[DI]
    JE DIR     
    ;____________                  
    ;Comparacion si la opc ing es 3
    LEA DI, TRES
    CMP AL, [DI]
    JE TEL 
    ;____________                  
    ;Comparacion si la opc ing es 4
    LEA DI, CUATRO
    CMP AL, [DI] 
    JE MOS   
    ;____________                  
    ;Comparacion si la opc ing es 5 
    LEA DI, CINCO
    CMP AL, [DI] 
    JE SALIR 
    CALL ERR
    
     
    inicioMenu endp


 
;______________________________
;es el submenu de nombre

 NOM:   CALL LIMPIAR
        call CURSOR
        CALL MOSNOM;etiqueta 
        CALL ENTRARNOM 
        CALL LIMPIAR
        CALL FINOM
       
        JMP inicioMenu       
;______________________________
;es el submenu de direccion
 
 DIR:   CALL LIMPIAR 
        call CURSOR
        CALL MOSDIR
        CALL ENTRARDIR
        CALL LIMPIAR
        CALL FINDIR
         
        JMP inicioMenu
        
;______________________________
;es el submenu de telefono

 TEL:   
        CALL LIMPIAR
        CALL CURSOR
        CALL MOSTELF
        CALL ENTRARTEL
        CALL LIMPIAR
        CALL FINTEL
        
        JMP inicioMenu
 
;______________________________
;es el submenu de mostrar
 
 MOS:   
        CALL LIMPIAR
        CALL CURSOR
        CALL CDATOS
        
        ;____________________
        ;muestra el nombre
        MOV DX,0403h
        CALL CURSOR1 
        CALL CNOMBRE 
        CALL INGRENOM
        
        ;____________________
        ;muestra la direccion
        MOV DX,0603h
        CALL CURSOR1
        CALL CDIRECCION 
        CALL INGREDIR
       
        ;____________________
        ;muestra el telefono
        MOV DX,0803h
        CALL CURSOR1
        CALL CTELEFONO
        CALL INGRETEL
        CALL PAUSA   
        
        ;____________________
        ;va al menu inicial
        CALL LIMPIAR
        CALL CURSOR
        
        JMP inicioMenu

;______________________________
;es el submenu de error

 ERR:    
        
        CALL MOSTRARERROR
        CALL PAUSA
        CALL LIMPIAR  
        CALL CURSOR 
        JMP inicioMenu

;______________________________
;es el submenu de la comparacion de ingreso de nombre

 INGRENOM: 
        LEA DX,GUARNOM
        CALL FINOM;finaliza la cadena
        cmp DX,' ';Compara si la cadena es vacia
        JNE  INDICARNOMBRE; si no es vacia indica lo ingresado 
        RET 
               
;______________________________
;es el submenu de la comparacion de ingreso de direccion 

 INGREDIR: 
        LEA DX,DGUARDAR 
        CALL  FINDIR
        cmp DX,' '
        JNE  INDICARDIRECCION
        RET   
;______________________________
;es el submenu de la comparacion de ingreso de direccion 
 
 INGRETEL:
        LEA DX,phone 
        CALL FINTEL
        cmp DX,' '
        JNE  INDICARTELEFONO
        RET              
           
END







