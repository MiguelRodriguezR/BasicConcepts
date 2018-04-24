-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-05-2016 a las 03:25:24
-- Versión del servidor: 5.6.26
-- Versión de PHP: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `restaurante`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE IF NOT EXISTS `cargos` (
  `nombre` varchar(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`nombre`, `id`) VALUES
('Chef', 1),
('Mesero', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE IF NOT EXISTS `clientes` (
  `nombre` varchar(11) NOT NULL,
  `apellido` varchar(11) NOT NULL,
  `cedula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consumos`
--

CREATE TABLE IF NOT EXISTS `consumos` (
  `id` int(11) NOT NULL,
  `plato` int(11) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tiquetera` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `consumos`
--

INSERT INTO `consumos` (`id`, `plato`, `fecha`, `tiquetera`) VALUES
(15, 10, '2016-05-17 06:08:35', 5),
(16, 9, '2016-05-17 06:08:40', 5),
(17, 10, '2016-05-17 06:08:47', 5),
(18, 10, '2016-05-17 06:08:52', 5),
(19, 6, '2016-05-17 06:09:50', 2),
(20, 8, '2016-05-17 06:10:00', 2),
(21, 4, '2016-05-17 06:10:13', 2),
(22, 7, '2016-05-17 06:10:23', 2),
(23, 4, '2016-05-17 06:11:37', 4),
(24, 7, '2016-05-17 06:11:42', 4),
(25, 6, '2016-05-17 06:11:48', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE IF NOT EXISTS `empleados` (
  `nombre` varchar(60) NOT NULL,
  `cedula` int(11) NOT NULL,
  `cargo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`nombre`, `cedula`, `cargo`) VALUES
('Miguel Rodriguez', 1085296784, 1),
('Camilo Rosales', 2120341250, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `platos`
--

CREATE TABLE IF NOT EXISTS `platos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `tipo` varchar(11) NOT NULL,
  `valor` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `platos`
--

INSERT INTO `platos` (`id`, `nombre`, `tipo`, `valor`) VALUES
(4, 'Ajiaco', '4', 8000),
(5, 'Helado Ron ', '2', 5000),
(6, 'Sancocho', '4', 10000),
(7, 'Bandeja Paisa', '4', 12000),
(8, 'Arroz con Posho', '4', 5000),
(9, 'Hamburguesa', '1', 2000),
(10, 'Perro Caliente', '1', 2000),
(11, '1/2 Old Park', '3', 30000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos`
--

CREATE TABLE IF NOT EXISTS `tipos` (
  `id` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipos`
--

INSERT INTO `tipos` (`id`, `tipo`) VALUES
(1, 'Comida rapida'),
(2, 'Heladeria'),
(3, 'Licor'),
(4, 'Almuerzo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiqueteras`
--

CREATE TABLE IF NOT EXISTS `tiqueteras` (
  `id` int(11) NOT NULL,
  `cliente` varchar(40) NOT NULL,
  `tamano` int(11) NOT NULL,
  `consumo` int(11) NOT NULL DEFAULT '0',
  `tipo` varchar(11) NOT NULL,
  `cedula` int(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tiqueteras`
--

INSERT INTO `tiqueteras` (`id`, `cliente`, `tamano`, `consumo`, `tipo`, `cedula`) VALUES
(2, 'Mario', 30, 4, '4', 12348764),
(3, 'Alfonso', 30, 0, '2', 54234235),
(4, 'Manuel', 3, 3, '4', 33312451),
(5, 'Ricardo Timaran', 40, 4, '1', 87934621);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `consumos`
--
ALTER TABLE `consumos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `platos`
--
ALTER TABLE `platos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipos`
--
ALTER TABLE `tipos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tiqueteras`
--
ALTER TABLE `tiqueteras`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `consumos`
--
ALTER TABLE `consumos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT de la tabla `platos`
--
ALTER TABLE `platos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT de la tabla `tipos`
--
ALTER TABLE `tipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `tiqueteras`
--
ALTER TABLE `tiqueteras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
