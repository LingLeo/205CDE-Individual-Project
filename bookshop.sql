-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 09, 2019 at 10:56 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookshop`
--
CREATE DATABASE IF NOT EXISTS `bookshop` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bookshop`;

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `Book_Key` int(5) NOT NULL,
  `Book_Name` varchar(100) NOT NULL,
  `Book_Author` varchar(40) NOT NULL,
  `Book_Publisher` varchar(40) NOT NULL,
  `Book_Description` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`Book_Key`, `Book_Name`, `Book_Author`, `Book_Publisher`, `Book_Description`) VALUES
(3001, 'Britain in Pictures: 1.Wild Life of Britain', 'F. Fraser Darling', 'London: William Collins', 'first book'),
(3002, 'Britain in Pictures: 2.Wild Life of Britain', 'F. Fraser Darling', 'London: William Collins', 'second book'),
(3003, 'Britain in Pictures: 3.Wild Life of Britain', 'F. Fraser Darling', 'London: William Collins', 'third book'),
(3004, 'Britain in Pictures: 4.Wild Life of Britain', 'F. Fraser Darling', 'London: William Collins', 'fourth book'),
(3005, '55a', '55b', '55c', '55d');

-- --------------------------------------------------------

--
-- Table structure for table `officer`
--

CREATE TABLE `officer` (
  `Officer_Key` int(5) NOT NULL,
  `Officer_Name` varchar(10) NOT NULL,
  `Officer_Login_Key` varchar(10) NOT NULL,
  `Officer_Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `officer`
--

INSERT INTO `officer` (`Officer_Key`, `Officer_Name`, `Officer_Login_Key`, `Officer_Password`) VALUES
(2001, 'LeoLee', 'LeoLee', 'LeoLee123'),
(2002, 'EdmondLee', 'EdmondLee', 'EdmondLee4'),
(2003, 'FokLee', 'FokLee', 'FokLee789'),
(2004, '44', '44aa', '44b');

-- --------------------------------------------------------

--
-- Table structure for table `reader`
--

CREATE TABLE `reader` (
  `Reader_Key` int(5) NOT NULL,
  `Reader_Login_Key` varchar(10) NOT NULL,
  `Reader_Password` varchar(10) NOT NULL,
  `Reader_Name` varchar(20) NOT NULL,
  `Reader_Sex` varchar(1) NOT NULL,
  `Reader_DOE` date NOT NULL,
  `Reader_Address` varchar(40) NOT NULL,
  `Reader_Phone_no` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reader`
--

INSERT INTO `reader` (`Reader_Key`, `Reader_Login_Key`, `Reader_Password`, `Reader_Name`, `Reader_Sex`, `Reader_DOE`, `Reader_Address`, `Reader_Phone_no`) VALUES
(1001, 'Carol', 'Carol123', 'Carol Lee', 'F', '2000-01-01', 'Shatin ', '12345678'),
(1002, 'Helen', 'Helen456', 'Helen Lee', 'F', '2000-01-02', 'Mei Foo', '23456790'),
(1003, 'GrandMa', 'GrandMa789', 'GrandMa Lee', 'F', '2000-01-03', 'MongKok', '34567901'),
(1004, 'lingleo', 'Kamenride1', 'Ling', 'M', '1998-11-07', '1', '2'),
(1005, '5a', '5b', '5c', '5', '1990-01-02', '5e', '5f'),
(1007, '5a', '5b', '5c', '5', '1990-01-02', '5e', '5f'),
(1008, '5a', '5b', '5c', '5', '1990-01-02', '5e', '5f'),
(1010, '5', '5a', '5b', '5', '1998-11-07', '5e', '5f'),
(1011, '5', '5a', '5b', '5', '1998-11-07', '5e', '5f'),
(1012, '5a', '5b', '5c', '5', '1990-01-02', '5e', '5f'),
(1013, '5', '5b', '5c', '5', '1990-01-02', '5e', '5f'),
(1014, '5', '5a', '5c', '5', '1990-01-02', '5e', '5f'),
(1015, '5', '5a', '5b', '5', '1990-01-02', '5e', '5f'),
(1016, '5', '5a', '5b', '5', '1990-01-02', '5e', '5f'),
(1017, '5', '5a', '5b', '5', '1990-01-02', '5e', '5f'),
(1018, '5', '5a', '5b', '5', '1990-01-02', '5e', '5f');

-- --------------------------------------------------------

--
-- Table structure for table `reserve`
--

CREATE TABLE `reserve` (
  `Reserve_Key` int(5) NOT NULL,
  `Reserve_Date` date NOT NULL,
  `Reader_Key` int(5) NOT NULL,
  `Book_Key` int(5) NOT NULL,
  `Officer_Key` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reserve`
--

INSERT INTO `reserve` (`Reserve_Key`, `Reserve_Date`, `Reader_Key`, `Book_Key`, `Officer_Key`) VALUES
(6001, '2018-10-31', 1001, 3001, 2001),
(6002, '2018-11-01', 1002, 3002, 2002),
(6003, '2018-11-02', 1003, 3003, 2003),
(6004, '1990-01-04', 1004, 3004, 2004);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`Book_Key`);

--
-- Indexes for table `officer`
--
ALTER TABLE `officer`
  ADD PRIMARY KEY (`Officer_Key`);

--
-- Indexes for table `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`Reader_Key`);

--
-- Indexes for table `reserve`
--
ALTER TABLE `reserve`
  ADD PRIMARY KEY (`Reserve_Key`),
  ADD KEY `Reader_Key` (`Reader_Key`),
  ADD KEY `Book_Key` (`Book_Key`),
  ADD KEY `Officer_Key` (`Officer_Key`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
