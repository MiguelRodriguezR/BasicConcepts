<?php

class modelo extends CI_Model{

  function __construct(){
    parent::__construct();
  }

  function consultar_usuarios(){

    $query =  $this->db->get('usuarios');
    return $query->result() ;
  }

  function pedir_captcha(){
    $captchas = array(
          0 => "urvtp",
          1 => "hatsm",
          2 => "w9nb4",
          3 => "tk58p",
          4 => "b4t9s",
          5 => "wb3cx",
          6 => "r48ek"
      );
    $r = rand(0, 6);
    return array( "id" =>$r, "val" =>$captchas[$r]);
  }


  function consultar_fechas(){

    $query =  $this->db->get('eventos');
    return $query->result() ;
  }

  function consultar_estudios(){
    $this->db->where('usuario', $this->session->cedula);
    $query =  $this->db->get('estudios');
    return $query->result() ;
  }

  function consultar_productividad(){
    $this->db->where('usuario', $this->session->cedula);
    $query =  $this->db->get('p_p');
    return $query->result() ;
  }


  function eliminar_usuariopc($ced){

    $this->db->where('cedula', $ced);
    $query = $this->db->delete('usuarios');
    //$query->result();
  }

  function consultar_usuariopc($ced){

    $this->db->where('cedula', $ced);
    $query =  $this->db->get('usuarios');
    foreach ($query->result() as $row){
        $res = array(
          'cedula' => $row->cedula,
          'tipo' => $row->tipo,
          'nombre' => $row->nombre,
          'apellido' => $row->apellido,
          'img' => $row->img
        );
    }
    return $res;
  }

  function consultar_usuario($e){

    $this->db->where('cedula', $e['cedula']);
    $query =  $this->db->get('usuarios');
    $res = array('cedula'=>"");
    foreach ($query->result() as $row){
      if($row->clave == $e['clave']){
        $res = array(
          'cedula' => $row->cedula,
          'tipo' => $row->tipo,
          'nombre' => $row->nombre,
          'apellido' => $row->apellido,
          'img' => $row->img
        );
      }
    }
    return $res;
  }

  function actualizar_foto(){
    $this->db->set('img',"p".$this->session->cedula);
    $this->db->where('cedula',$this->session->cedula);
    $this->db->update('usuarios');
  }

  function modificar_usuario($e){

    $this->db->set('nombre',$e["nombre"]);
    $this->db->set('apellido',$e["apellido"]);
    if($e["clave_n"]!=""){
      $this->db->set('clave',$e["clave_n"]);
    }
    $this->db->where('cedula',$this->session->cedulau);
    $this->db->update('usuarios');
  }

  function actualizar_nombre($e){

    $isOk=0;
    if($e["clave_a"]!=""){
      $this->db->where('cedula', $this->session->cedula);
      $query =  $this->db->get('usuarios');
      foreach ($query->result() as $row){
        if($row->clave == $e['clave_a']){
          $isOk=1;
        }
      }
    }


    $this->db->set('nombre',$e["nombre"]);
    $this->db->set('apellido',$e["apellido"]);
    if($isOk==1){
      $this->db->set('clave',$e["clave_n"]);
    }
    $this->db->where('cedula',$this->session->cedula);
    $this->db->update('usuarios');
  }

  function agregar_usuario($e){
    $data = array(
      'cedula' => $e["cedula"],
      'nombre' => $e["nombre"],
      'apellido' => $e["apellido"],
      'clave' => $e["cedula"],
      'tipo' => $e["tipo"],
      'img' => 'alien'
    );
    $this->db->insert('usuarios',$data);
    return "exito";
  }

  function crear_evento($e){

    $data = array(
      'nombre' => $e["nombre"],
      'tipo' => $e["tipo"],
      'lugar' => $e["lugar"],
      'fecha_inicio' => $e["fecha_i"],
      'fecha_final' => $e["fecha_f"],
      'valor_inscripcion' => $e["valor"]
    );
    $this->db->insert('eventos',$data);
    return "exito al registrar el evento";
  }

  function agregar_estudios($e){

    $data = array(
      'usuario' => $this->session->cedula,
      'grado' => $e["grado"],
      'titulo' => $e["titulo"],
      'fecha_grado' => $e["fecha_g"],
      'modalidad' => $e["modalidad"]
    );
    $this->db->insert('estudios',$data);
    return "exito al registrar el evento";
  }

  function agregar_productividad($e){

    $data = array(
      'usuario' => $this->session->cedula,
      'tipo' => $e["tipo"],
      'titulo' => $e["titulo"],
      'fecha_realizacion' => $e["fecha_r"],
      'lugar_desarrollo' => $e["lugar"],
      'descripcion' => $e["descripcion"],
      'certificado' => "d".$this->session->cedula."-".$e["fecha_r"]
    );
    $this->db->insert('p_p',$data);
    return "exito al registrar la productividad";
  }

}


?>
