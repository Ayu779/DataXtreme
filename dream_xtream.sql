-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 16, 2020 at 09:12 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dream_xtream`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand_detail`
--

CREATE TABLE `brand_detail` (
  `company_id` bigint(20) NOT NULL,
  `brand_name` varchar(255) NOT NULL,
  `parent_company` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `brand_detail`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_accounting_detail`
--

CREATE TABLE `company_accounting_detail` (
  `company_id` bigint(20) NOT NULL,
  `GSTIN_number` varchar(15) DEFAULT NULL,
  `PAN_number` varchar(15) DEFAULT NULL,
  `TAN_number` varchar(15) DEFAULT NULL,
  `type_of_registration` varchar(255) NOT NULL,
  `applicability_date` date DEFAULT NULL,
  `annual_turn_over` double DEFAULT NULL,
  `TDS` float DEFAULT NULL,
  `TCS` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `company_accounting_detail`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_info`
--

CREATE TABLE `company_info` (
  `email` varchar(255) NOT NULL,
  `company_id` bigint(20) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `accounting_year` date NOT NULL,
  `book_beginning_year` date NOT NULL,
  `mailing_name` varchar(255) DEFAULT NULL,
  `type_of_business` varchar(255) DEFAULT NULL,
  `mobile_no` int(14) NOT NULL,
  `another_mobile_no` int(14) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `company_mail` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `currency_symbol` varchar(5) DEFAULT NULL,
  `formal_name` varchar(255) DEFAULT NULL,
  `add_currency_symbol_to_amount` varchar(20) DEFAULT NULL,
  `add_space_between_symbol_and_amount` varchar(20) DEFAULT NULL,
  `display_amount_in_millions` varchar(20) DEFAULT NULL,
  `decimal_places_for_amount` varchar(20) DEFAULT NULL,
  `word_representing_amount_after_decimal_places` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `company_info`:
--   `email`
--       `owner_account` -> `email`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_ledgers`
--

CREATE TABLE `company_ledgers` (
  `company_id` bigint(20) NOT NULL,
  `ledger_name` varchar(255) NOT NULL,
  `group_under` varchar(255) NOT NULL,
  `date_of_creation` date NOT NULL,
  `opening_balance` double DEFAULT NULL,
  `is_inventory_value_affected` varchar(255) DEFAULT NULL,
  `ledger_type` varchar(255) DEFAULT NULL,
  `rounding_method` varchar(255) DEFAULT NULL,
  `rounding_limit` int(11) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `company_ledgers`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `custom_group_detail`
--

CREATE TABLE `custom_group_detail` (
  `company_id` bigint(20) NOT NULL,
  `group_name` varchar(255) NOT NULL,
  `group_under` varchar(255) NOT NULL,
  `date_of_creation` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `custom_group_detail`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `godown_detail`
--

CREATE TABLE `godown_detail` (
  `company_id` bigint(20) NOT NULL,
  `godown_name` varchar(255) NOT NULL,
  `under` varchar(255) DEFAULT NULL,
  `date_of_creation` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `godown_detail`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `owner_account`
--

CREATE TABLE `owner_account` (
  `email` varchar(255) NOT NULL,
  `owner_name` varchar(255) NOT NULL,
  `mobile_no` int(14) NOT NULL,
  `another_mobile_no` int(14) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `password` varchar(255) NOT NULL,
  `signature` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `owner_account`:
--

-- --------------------------------------------------------

--
-- Table structure for table `stock_category`
--

CREATE TABLE `stock_category` (
  `company_id` bigint(20) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `category_under` varchar(255) NOT NULL,
  `date_of_creation` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `stock_category`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `stock_group`
--

CREATE TABLE `stock_group` (
  `company_id` bigint(20) NOT NULL,
  `group_name` varchar(255) NOT NULL,
  `group_under` varchar(255) NOT NULL,
  `group_under_custom` varchar(255) DEFAULT NULL,
  `should_quantities_of_items_to_be_added` varchar(255) NOT NULL,
  `date_of_creation` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `stock_group`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `stock_items`
--

CREATE TABLE `stock_items` (
  `company_id` bigint(20) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `code_number` varchar(255) DEFAULT NULL,
  `date_of_creation` date NOT NULL,
  `under_stock_group` varchar(255) DEFAULT NULL,
  `under_stock_category` varchar(255) DEFAULT NULL,
  `under_brand` varchar(255) DEFAULT NULL,
  `unit_of_item` varchar(255) DEFAULT NULL,
  `ob_quantity` float DEFAULT NULL,
  `ob_price` float DEFAULT NULL,
  `pp_quantity` float DEFAULT NULL,
  `pp_price` float DEFAULT NULL,
  `sp_quantity` float DEFAULT NULL,
  `sp_price` float DEFAULT NULL,
  `rate_of_duty` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `stock_items`:
--   `company_id`
--       `company_info` -> `company_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `unit_of_measure`
--

CREATE TABLE `unit_of_measure` (
  `company_id` bigint(20) NOT NULL,
  `type_of_unit` varchar(255) NOT NULL,
  `symbol` varchar(255) DEFAULT NULL,
  `formal_name` varchar(255) DEFAULT NULL,
  `SKU` varchar(255) DEFAULT NULL,
  `number_of_decimal_places` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `unit_of_measure`:
--   `company_id`
--       `company_info` -> `company_id`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand_detail`
--
ALTER TABLE `brand_detail`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `company_accounting_detail`
--
ALTER TABLE `company_accounting_detail`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `company_info`
--
ALTER TABLE `company_info`
  ADD PRIMARY KEY (`company_id`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `company_ledgers`
--
ALTER TABLE `company_ledgers`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `custom_group_detail`
--
ALTER TABLE `custom_group_detail`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `godown_detail`
--
ALTER TABLE `godown_detail`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `owner_account`
--
ALTER TABLE `owner_account`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `stock_category`
--
ALTER TABLE `stock_category`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `stock_group`
--
ALTER TABLE `stock_group`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `stock_items`
--
ALTER TABLE `stock_items`
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `unit_of_measure`
--
ALTER TABLE `unit_of_measure`
  ADD KEY `company_id` (`company_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company_info`
--
ALTER TABLE `company_info`
  MODIFY `company_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `brand_detail`
--
ALTER TABLE `brand_detail`
  ADD CONSTRAINT `brand_detail_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `company_accounting_detail`
--
ALTER TABLE `company_accounting_detail`
  ADD CONSTRAINT `company_accounting_detail_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `company_info`
--
ALTER TABLE `company_info`
  ADD CONSTRAINT `company_info_ibfk_1` FOREIGN KEY (`email`) REFERENCES `owner_account` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `company_ledgers`
--
ALTER TABLE `company_ledgers`
  ADD CONSTRAINT `company_ledgers_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `custom_group_detail`
--
ALTER TABLE `custom_group_detail`
  ADD CONSTRAINT `custom_group_detail_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `godown_detail`
--
ALTER TABLE `godown_detail`
  ADD CONSTRAINT `godown_detail_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `stock_category`
--
ALTER TABLE `stock_category`
  ADD CONSTRAINT `stock_category_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `stock_group`
--
ALTER TABLE `stock_group`
  ADD CONSTRAINT `stock_group_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `stock_items`
--
ALTER TABLE `stock_items`
  ADD CONSTRAINT `stock_items_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `unit_of_measure`
--
ALTER TABLE `unit_of_measure`
  ADD CONSTRAINT `unit_of_measure_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company_info` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
