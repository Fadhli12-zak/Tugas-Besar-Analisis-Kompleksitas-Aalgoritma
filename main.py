from algoritma.iteratif import iteratifAlgo
from algoritma.rekursif import rekursif_sequential_search
import matplotlib.pyplot as plt
import time

kost_list = [
  "Kost Paviliun Pondok Al Affan", "Kost UZ", "Kost Violet", "Kost Bougenville", "Kost Bumi Kiara","Kost Puri Indah 3", "Kost Wisma Citra", "Kost Puri Indah 3", "Villa Zone Kost", "Kost Pondok Amanah",
    "Kost Roemah Kita", "Kost Rumah Sazira","Kost Wisma Lentera Bandung DayeuhKolot","Kost Sky Garden Logam Bojongsoang","Kost Pondok Indriati 1 DayeuhKolot Bandung", "Kost Rumah Sazira Bojongsoang","Kost Caliahomestay",
    "Kost Zayn","Kost Anna", "Kost Sazira","Sriwijaya Residence Regol","Kost Elok House Batununggal","Amoris Kos","Singgahsini Kost","Kost Pondok Indriati", "Kost Anna", "Kost Umi", "Kost The QIM Student Habitation",
    "Kost Wisma Arnatja","Kost Ibu Pandji","Kost Genius","Kost Syach Room 1","Kost Syach Room 2","Kost Qubilah","Kost Eksklusif Batununggal", "Kost Tify Bojongsoang", "Kost Momikyu GH","Kost Dorminary", "Kost Wisma Lentera",
    "Kost Wisma Maulana", "Kost Pondok Naturaliza","Kost Pondok Vanboo Dayeuhkolot","Kost Raflesia 2","Kost Raflesia 1","Kost Dewata", "Kost Yeoja II","Kost Puri Indah 2","Kost Puri Indah 1","Kost Bagja 1 Bojongsoang",
    "Kost bagja 2 bojongsoang","Kost Harmony Bandung", "Kost Green Bamboo","Kost Taman Sari","Kost Citra Gading", "Kost Graha Mandiri","Kost Melati","Kost Sakura", "Kost Anggrek",  "Kost Taman Wisma", "Kost Santika Bandung",
    "Kost Arjuna",    "Kost Surya Mandala","Kost Rajawali","Kost Intan Permata","Kost Seruni","Kost Griya Lestari","Kost Buana Loka", "Kost Permata Hijau","Kost Mega Citra",  "Kost Grand Pavilion","Kost Asri Bojongsoang",
    "Kost Jaya Sentosa","Kost Golden Leaf","Kost Cendana Residence","Kost Wijaya Kusuma","Kost Alamanda","Kost Flamboyan","Kost Kenanga", "Kost Pesona Indah", "Kost Pondok Jati", "Kost Prima Loka", "Kost Madani Bandung", 
    "Kost Aster","Kost Green Harmony", "Kost Delima", "Kost Galaxy","Kost Green Terrace","Kost Edelweiss", "Kost Mutiara Bandung","Kost Pondok Ceria","Kost Sky Residence","Kost Lembayung","Kost Lotus","Kost Palem Asri",
    "Kost Manglayang", "Kost Padjadjaran", "Kost Graha Permata", "Kost Safira","Kost Taruna", "Kost Ambarwati","Kost Graha Dayeuhkolot 14","Kost Buah Batu Sinar 2" ,"Kost Taman Sinar Buah Batu 3","Kost Pondok Buah Batu 13",
    "Kost Green Harmony Dayeuhkolot 2", "Kost Sakura Buah Batu 4","Kost Buah Batu Lestari 2","Kost Dayeuhkolot Green Valley 2","Kost Graha Buah Batu 15", "Kost Pondok Cendana Dayeuhkolot",  "Kost Taman Buah Batu 9",
    "Kost Green Terrace Buah Batu", "Kost Dayeuhkolot Ceria 4","Kost Buah Batu Mandiri 3",  "Kost Sakura Dayeuhkolot 5", "Kost Pondok Buah Batu 14", "Kost Dayeuhkolot Nirwana 2", "Kost Graha Citra Buah Batu",
    "Kost Graha Buah Batu 16",  "Kost Pondok Buah Batu 15","Kost Green Valley Buah Batu 3","Kost Sakura Graha Dayeuhkolot", "Kost Buah Batu Sejahtera 4", "Kost Green Dayeuhkolot 2", "Kost Pondok Buah Batu 16",
    "Kost Sakura Buah Batu 5","Kost Taman Buah Batu 10", "Kost Buah Batu Jaya", "Kost Pondok Green Dayeuhkolot", "Kost Graha Dayeuhkolot 17","Kost Green Sinar Buah Batu",  "Kost Pondok Buah Batu 17",
    "Kost Sakura Citra Buah Batu", "Kost Buah Batu Harmoni 3","Kost Green Buah Batu 7","Kost Buah Batu Nirwana 3","Kost Pondok Green Buah Batu", "Kost Dayeuhkolot Cerah 3",  "Kost Taman Cendana Dayeuhkolot 2"
    "Kost Dayeuhkolot Green 3","Kost Pondok Buah Batu 18","Kost Graha Dayeuhkolot 18","Kost Sakura Dayeuhkolot 6","Kost Taman Dayeuhkolot 5","Kost Sakura Dayeuhkolot 7","Kost Buah Batu Lestari 3",
    "Kost Graha Buah Batu 19","Kost Buah Batu Sejahtera 5","Kost Pondok Buah Batu 19","Kost Green Residence Dayeuhkolot 3","Kost Taman Buah Batu 11","Kost Pondok Buah Batu 20", "Kost Dayeuhkolot Sinar 2",
    "Kost Dayeuhkolot Sejahtera 6","Kost Sakura Graha Dayeuhkolot 2","Kost Buah Batu Mandiri 4", "Kost Pondok Buah Batu 21","Kost Taman Buah Batu 12","Kost Green Valley Dayeuhkolot 4","Kost Graha Dayeuhkolot 21",
    "Kost Graha Buah Batu 20","Kost Sakura Buah Batu 6","Kost Pondok Dayeuhkolot 6","Kost Buah Batu Raya 5","Kost Pondok Citra Buah Batu", "Kost Sakura Buah Batu 7","Kost Green Terrace Dayeuhkolot 2", "Kost Buah Batu Nirwana 4",
    "Kost Green Buah Batu 8","Kost Taman Dayeuhkolot 6","Kost Graha Buah Batu 22","Kost Pondok Buah Batu 22","Kost Dayeuhkolot Harmoni 4","Kost Graha Dayeuhkolot 23","Kost Taman Buah Batu 13","Kost Pondok Green Dayeuhkolot 2",
    "Kost Graha Buah Batu 23","Kost Pondok Buah Batu 23","Kost Buah Batu Harmoni 4","Kost Green Buah Batu 9","Kost Pondok Buah Batu 24","Kost Sakura Buah Batu 8","Kost Graha Dayeuhkolot 24","Kost Taman Dayeuhkolot 7","Kost Pondok Buah Batu 25",
    "Kost Green Valley Dayeuhkolot 5","Kost Sakura Dayeuhkolot 9","Kost Graha Buah Batu 24","Kost Sakura Dayeuhkolot 8","Kost Dayeuhkolot Lestari 4", "Kost Sakura Graha Dayeuhkolot","Kost Pondok Green Buah Batu 2",
    "Kost Pondok Buah Batu 26","Kost Taman Buah Batu 14","Kost Sakura Buah Batu 9", "Kost Green Residence Buah Batu","Kost Pondok Buah Batu 27", "Kost Graha Dayeuhkolot 25", "Kost Taman Dayeuhkolot 8", "Kost Pondok Buah Batu 28","Kost Graha Buah Batu 25",
    "Kost Dayeuhkolot Green Valley 3", "Kost Sakura Graha Buah Batu","Kost Green Buah Batu 11","Kost Taman Buah Batu 15","Kost Pondok Buah Batu 30","Kost Graha Dayeuhkolot 27", "Kost Sakura Buah Batu 11","Kost Pondok Buah Batu 33",
    "Kost Sakura Buah Batu 10","Kost Buah Batu Sinar 3","Kost Green Buah Batu 10","Kost Pondok Dayeuhkolot 7","Kost Graha Buah Batu 26","Kost Sakura Dayeuhkolot 10","Kost Buah Batu Mandiri 5",  "Kost Pondok Buah Batu 29",
    "Kost Pondok Graha Dayeuhkolot","Kost Green Valley Buah Batu 6","Kost Buah Batu Sejahtera 6","Kost Sakura Dayeuhkolot 11","Kost Pondok Buah Batu 31", "Kost Graha Buah Batu 27","Kost Dayeuhkolot Sinar 3","Kost Green Buah Batu 12",
    "Kost Sakura Graha Dayeuhkolot 2","Kost Pondok Buah Batu 32","Kost Dayeuhkolot Lestari 5","Kost Taman Buah Batu 16","Kost Pondok Dayeuhkolot 8", "Kost Graha Buah Batu 28","Kost Sakura Buah Batu 12","Kost Green Residence Dayeuhkolot 4",
    "Kost Graha Dayeuhkolot 29","Kost Sakura Dayeuhkolot 12""Kost Pondok Buah Batu 34","Kost Taman Sinar Buah Batu 4","Kost Dayeuhkolot Harmoni 5","Kost Graha Buah Batu 29","Kost Green Terrace Buah Batu"
    "Kost Sakura Buah Batu 13", "Kost Pondok Buah Batu 35", "Kost Graha Dayeuhkolot 30", "Kost Graha Buah Batu 30", "Kost Pondok Buah Batu 36", "Kost Dayeuhkolot Green 4", "Kost Dayeuhkolot Indah 3", "Kost Taman Sinar Dayeuhkolot 2", "Kost Graha Dayeuhkolot 8", 
    "Kost Taman Buah Batu 17", "Kost Pondok Green Buah Batu 3", "Kost Sakura Dayeuhkolot 13", "Kost Sakura Graha Dayeuhkolot", "Kost Pondok Buah Batu 7", "Kost Buah Batu Modern 2", 
    "Kost Pondok Buah Batu 8", "Kost Green Valley Dayeuhkolot 2", "Kost Buah Batu Premium 2",  "Kost Dayeuhkolot Mandiri 2", "Kost Sakura Dayeuhkolot 3", "Kost Pondok Harmoni Buah Batu", 
    "Kost Green Buah Batu 5", "Kost Graha Buah Batu 10", "Kost Dayeuhkolot Taman Cendana",   "Kost Griya Citra Buah Batu", "Kost Puri Dayeuhkolot 7", "Kost Pondok Buah Batu 9",
    "Kost Green Valley Buah Batu", "Kost Buah Batu Nirwana 2", "Kost Graha Buah Batu 11", "Kost Sakura Buah Batu 3", "Kost Buah Batu Raya 4", "Kost Taman Buah Batu 7",
    "Kost Dayeuhkolot Ceria 3", "Kost Pondok Sari Buah Batu 3", "Kost Graha Sentosa Dayeuhkolot 2","Kost Dayeuhkolot Anggrek", "Kost Green Buah Batu 6", "Kost Puri Buah Batu 4",
    "Kost Taman Dayeuhkolot 4", "Kost Pondok Buah Batu 10", "Kost Graha Cendana Buah Batu","Kost Dayeuhkolot Lestari 3", "Kost Buah Batu Asri 3", "Kost Sakura Dayeuhkolot 4",
    "Kost Graha Buah Batu 12", "Kost Taman Cendana Dayeuhkolot", "Kost Pondok Buah Batu 11", "Kost Dayeuhkolot Sejahtera 2", "Kost Green Hills Buah Batu 2", "Kost Graha Sentosa Buah Batu 2",
    "Kost Taman Buah Batu 8", "Kost Sakura Cerah Dayeuhkolot 2", "Kost Buah Batu Sari 3","Kost Pondok Dayeuhkolot 4", "Kost Graha Buah Batu 13", "Kost Buah Batu Sejahtera 3","Kost Dayeuhkolot Harmoni 3", "Kost Green Valley Dayeuhkolot 3", "Kost Pondok Buah Batu 12",
    "Kost Taman Buah Batu 4", "Kost Griya Buah Batu 4", "Kost Dayeuhkolot Asri 3","Kost Buah Batu Sentosa 3", "Kost Graha Dayeuhkolot 5", "Kost Buah Batu Raya 2",
    "Kost Dayeuhkolot Sentosa", "Kost Graha Buah Batu 5", "Kost Puri Dayeuhkolot 4","Kost Green Valley Dayeuhkolot", "Kost Griya Alam Buah Batu", "Kost Dayeuhkolot Indah 2","Kost Green Residence Buah Batu", "Kost Sakura Dayeuhkolot 2", "Kost Buah Batu Megah", "Kost Taman Indah Buah Batu", "Kost Dayeuhkolot Melati 2", "Kost Griya Sentosa Buah Batu",
    "Kost Pondok Dayeuhkolot 3", "Kost Buah Batu Sejahtera 2", "Kost Taman Cendana Buah Batu","Kost Green Harmony Dayeuhkolot", "Kost Puri Buah Batu 2", "Kost Sakura Buah Batu",
    "Kost Griya Citra Dayeuhkolot", "Kost Buah Batu Mandiri 2", "Kost Green Buah Batu 3","Kost Dayeuhkolot Prima 2", "Kost Buah Batu Sinar", "Kost Graha Harmoni Dayeuhkolot",
    "Kost Pondok Buah Batu 3", "Kost Dayeuhkolot Ceria 2", "Kost Taman Buah Batu 5","Kost Green Residence Dayeuhkolot", "Kost Buah Batu Maju", "Kost Dayeuhkolot Nirwana", "Kost AZ ciganitri"
     "Kost Paviliun Pondok Al Affan", "Kost UZ", "Kost Violet", "Kost Bougenville", "Kost Bumi Kiara","Kost Puri Indah 3", "Kost Wisma Citra", "Kost Puri Indah 3", "Villa Zone Kost", "Kost Pondok Amanah",
    "Kost Roemah Kita", "Kost Rumah Sazira","Kost Wisma Lentera Bandung DayeuhKolot","Kost Sky Garden Logam Bojongsoang","Kost Pondok Indriati 1 DayeuhKolot Bandung", "Kost Rumah Sazira Bojongsoang","Kost Caliahomestay",
    "Kost Zayn","Kost Anna", "Kost Sazira","Sriwijaya Residence Regol","Kost Elok House Batununggal","Amoris Kos","Singgahsini Kost","Kost Pondok Indriati", "Kost Anna", "Kost Umi", "Kost The QIM Student Habitation",
    "Kost Wisma Arnatja","Kost Ibu Pandji","Kost Genius","Kost Syach Room 1","Kost Syach Room 2","Kost Qubilah","Kost Eksklusif Batununggal", "Kost Tify Bojongsoang", "Kost Momikyu GH","Kost Dorminary", "Kost Wisma Lentera",
    "Kost Wisma Maulana", "Kost Pondok Naturaliza","Kost Pondok Vanboo Dayeuhkolot","Kost Raflesia 2","Kost Raflesia 1","Kost Dewata", "Kost Yeoja II","Kost Puri Indah 2","Kost Puri Indah 1","Kost Bagja 1 Bojongsoang",
    "Kost bagja 2 bojongsoang","Kost Harmony Bandung", "Kost Green Bamboo","Kost Taman Sari","Kost Citra Gading", "Kost Graha Mandiri","Kost Melati","Kost Sakura", "Kost Anggrek",  "Kost Taman Wisma", "Kost Santika Bandung",
    "Kost Arjuna",    "Kost Surya Mandala","Kost Rajawali","Kost Intan Permata","Kost Seruni","Kost Griya Lestari","Kost Buana Loka", "Kost Permata Hijau","Kost Mega Citra",  "Kost Grand Pavilion","Kost Asri Bojongsoang",
    "Kost Jaya Sentosa","Kost Golden Leaf","Kost Cendana Residence","Kost Wijaya Kusuma","Kost Alamanda","Kost Flamboyan","Kost Kenanga", "Kost Pesona Indah", "Kost Pondok Jati", "Kost Prima Loka", "Kost Madani Bandung", 
    "Kost Aster","Kost Green Harmony", "Kost Delima", "Kost Galaxy","Kost Green Terrace","Kost Edelweiss", "Kost Mutiara Bandung","Kost Pondok Ceria","Kost Sky Residence","Kost Lembayung","Kost Lotus","Kost Palem Asri",
    "Kost Manglayang", "Kost Padjadjaran", "Kost Graha Permata", "Kost Safira","Kost Taruna", "Kost Ambarwati","Kost Graha Dayeuhkolot 14","Kost Buah Batu Sinar 2" ,"Kost Taman Sinar Buah Batu 3","Kost Pondok Buah Batu 13",
    "Kost Green Harmony Dayeuhkolot 2", "Kost Sakura Buah Batu 4","Kost Buah Batu Lestari 2","Kost Dayeuhkolot Green Valley 2","Kost Graha Buah Batu 15", "Kost Pondok Cendana Dayeuhkolot",  "Kost Taman Buah Batu 9",
    "Kost Green Terrace Buah Batu", "Kost Dayeuhkolot Ceria 4","Kost Buah Batu Mandiri 3",  "Kost Sakura Dayeuhkolot 5", "Kost Pondok Buah Batu 14", "Kost Dayeuhkolot Nirwana 2", "Kost Graha Citra Buah Batu",
    "Kost Graha Buah Batu 16",  "Kost Pondok Buah Batu 15","Kost Green Valley Buah Batu 3","Kost Sakura Graha Dayeuhkolot", "Kost Buah Batu Sejahtera 4", "Kost Green Dayeuhkolot 2", "Kost Pondok Buah Batu 16",
    "Kost Sakura Buah Batu 5","Kost Taman Buah Batu 10", "Kost Buah Batu Jaya", "Kost Pondok Green Dayeuhkolot", "Kost Graha Dayeuhkolot 17","Kost Green Sinar Buah Batu",  "Kost Pondok Buah Batu 17",
    "Kost Sakura Citra Buah Batu", "Kost Buah Batu Harmoni 3","Kost Green Buah Batu 7","Kost Buah Batu Nirwana 3","Kost Pondok Green Buah Batu", "Kost Dayeuhkolot Cerah 3",  "Kost Taman Cendana Dayeuhkolot 2"
    "Kost Dayeuhkolot Green 3","Kost Pondok Buah Batu 18","Kost Graha Dayeuhkolot 18","Kost Sakura Dayeuhkolot 6","Kost Taman Dayeuhkolot 5","Kost Sakura Dayeuhkolot 7","Kost Buah Batu Lestari 3",
    "Kost Graha Buah Batu 19","Kost Buah Batu Sejahtera 5","Kost Pondok Buah Batu 19","Kost Green Residence Dayeuhkolot 3","Kost Taman Buah Batu 11","Kost Pondok Buah Batu 20", "Kost Dayeuhkolot Sinar 2",
    "Kost Dayeuhkolot Sejahtera 6","Kost Sakura Graha Dayeuhkolot 2","Kost Buah Batu Mandiri 4", "Kost Pondok Buah Batu 21","Kost Taman Buah Batu 12","Kost Green Valley Dayeuhkolot 4","Kost Graha Dayeuhkolot 21",
    "Kost Graha Buah Batu 20","Kost Sakura Buah Batu 6","Kost Pondok Dayeuhkolot 6","Kost Buah Batu Raya 5","Kost Pondok Citra Buah Batu", "Kost Sakura Buah Batu 7","Kost Green Terrace Dayeuhkolot 2", "Kost Buah Batu Nirwana 4",
    "Kost Green Buah Batu 8","Kost Taman Dayeuhkolot 6","Kost Graha Buah Batu 22","Kost Pondok Buah Batu 22","Kost Dayeuhkolot Harmoni 4","Kost Graha Dayeuhkolot 23","Kost Taman Buah Batu 13","Kost Pondok Green Dayeuhkolot 2",
    "Kost Graha Buah Batu 23","Kost Pondok Buah Batu 23","Kost Buah Batu Harmoni 4","Kost Green Buah Batu 9","Kost Pondok Buah Batu 24","Kost Sakura Buah Batu 8","Kost Graha Dayeuhkolot 24","Kost Taman Dayeuhkolot 7","Kost Pondok Buah Batu 25",
    "Kost Green Valley Dayeuhkolot 5","Kost Sakura Dayeuhkolot 9","Kost Graha Buah Batu 24","Kost Sakura Dayeuhkolot 8","Kost Dayeuhkolot Lestari 4", "Kost Sakura Graha Dayeuhkolot","Kost Pondok Green Buah Batu 2",
    "Kost Pondok Buah Batu 26","Kost Taman Buah Batu 14","Kost Sakura Buah Batu 9", "Kost Green Residence Buah Batu","Kost Pondok Buah Batu 27", "Kost Graha Dayeuhkolot 25", "Kost Taman Dayeuhkolot 8", "Kost Pondok Buah Batu 28","Kost Graha Buah Batu 25",
    "Kost Dayeuhkolot Green Valley 3", "Kost Sakura Graha Buah Batu","Kost Green Buah Batu 11","Kost Taman Buah Batu 15","Kost Pondok Buah Batu 30","Kost Graha Dayeuhkolot 27", "Kost Sakura Buah Batu 11","Kost Pondok Buah Batu 33",
    "Kost Sakura Buah Batu 10","Kost Buah Batu Sinar 3","Kost Green Buah Batu 10","Kost Pondok Dayeuhkolot 7","Kost Graha Buah Batu 26","Kost Sakura Dayeuhkolot 10","Kost Buah Batu Mandiri 5",  "Kost Pondok Buah Batu 29",
    "Kost Pondok Graha Dayeuhkolot","Kost Green Valley Buah Batu 6","Kost Buah Batu Sejahtera 6","Kost Sakura Dayeuhkolot 11","Kost Pondok Buah Batu 31", "Kost Graha Buah Batu 27","Kost Dayeuhkolot Sinar 3","Kost Green Buah Batu 12",
    "Kost Sakura Graha Dayeuhkolot 2","Kost Pondok Buah Batu 32","Kost Dayeuhkolot Lestari 5","Kost Taman Buah Batu 16","Kost Pondok Dayeuhkolot 8", "Kost Graha Buah Batu 28","Kost Sakura Buah Batu 12","Kost Green Residence Dayeuhkolot 4",
    "Kost Graha Dayeuhkolot 29","Kost Sakura Dayeuhkolot 12""Kost Pondok Buah Batu 34","Kost Taman Sinar Buah Batu 4","Kost Dayeuhkolot Harmoni 5","Kost Graha Buah Batu 29","Kost Green Terrace Buah Batu"
    "Kost Sakura Buah Batu 13", "Kost Pondok Buah Batu 35", "Kost Graha Dayeuhkolot 30", "Kost Graha Buah Batu 30", "Kost Pondok Buah Batu 36", "Kost Dayeuhkolot Green 4", "Kost Dayeuhkolot Indah 3", "Kost Taman Sinar Dayeuhkolot 2", "Kost Graha Dayeuhkolot 8", 
    "Kost Taman Buah Batu 17", "Kost Pondok Green Buah Batu 3", "Kost Sakura Dayeuhkolot 13", "Kost Sakura Graha Dayeuhkolot", "Kost Pondok Buah Batu 7", "Kost Buah Batu Modern 2", 
    "Kost Pondok Buah Batu 8", "Kost Green Valley Dayeuhkolot 2", "Kost Buah Batu Premium 2",  "Kost Dayeuhkolot Mandiri 2", "Kost Sakura Dayeuhkolot 3", "Kost Pondok Harmoni Buah Batu", 
    "Kost Green Buah Batu 5", "Kost Graha Buah Batu 10", "Kost Dayeuhkolot Taman Cendana",   "Kost Griya Citra Buah Batu", "Kost Puri Dayeuhkolot 7", "Kost Pondok Buah Batu 9",
    "Kost Green Valley Buah Batu", "Kost Buah Batu Nirwana 2", "Kost Graha Buah Batu 11", "Kost Sakura Buah Batu 3", "Kost Buah Batu Raya 4", "Kost Taman Buah Batu 7",
    "Kost Dayeuhkolot Ceria 3", "Kost Pondok Sari Buah Batu 3", "Kost Graha Sentosa Dayeuhkolot 2","Kost Dayeuhkolot Anggrek", "Kost Green Buah Batu 6", "Kost Puri Buah Batu 4",
    "Kost Taman Dayeuhkolot 4", "Kost Pondok Buah Batu 10", "Kost Graha Cendana Buah Batu","Kost Dayeuhkolot Lestari 3", "Kost Buah Batu Asri 3", "Kost Sakura Dayeuhkolot 4",
    "Kost Graha Buah Batu 12", "Kost Taman Cendana Dayeuhkolot", "Kost Pondok Buah Batu 11", "Kost Dayeuhkolot Sejahtera 2", "Kost Green Hills Buah Batu 2", "Kost Graha Sentosa Buah Batu 2",
    "Kost Taman Buah Batu 8", "Kost Sakura Cerah Dayeuhkolot 2", "Kost Buah Batu Sari 3","Kost Pondok Dayeuhkolot 4", "Kost Graha Buah Batu 13", "Kost Buah Batu Sejahtera 3","Kost Dayeuhkolot Harmoni 3", "Kost Green Valley Dayeuhkolot 3", "Kost Pondok Buah Batu 12",
    "Kost Taman Buah Batu 4", "Kost Griya Buah Batu 4", "Kost Dayeuhkolot Asri 3","Kost Buah Batu Sentosa 3", "Kost Graha Dayeuhkolot 5", "Kost Buah Batu Raya 2",
    "Kost Dayeuhkolot Sentosa", "Kost Graha Buah Batu 5", "Kost Puri Dayeuhkolot 4","Kost Green Valley Dayeuhkolot", "Kost Griya Alam Buah Batu", "Kost Dayeuhkolot Indah 2","Kost Green Residence Buah Batu", "Kost Sakura Dayeuhkolot 2", "Kost Buah Batu Megah", "Kost Taman Indah Buah Batu", "Kost Dayeuhkolot Melati 2", "Kost Griya Sentosa Buah Batu",
    "Kost Pondok Dayeuhkolot 3", "Kost Buah Batu Sejahtera 2", "Kost Taman Cendana Buah Batu","Kost Green Harmony Dayeuhkolot", "Kost Puri Buah Batu 2", "Kost Sakura Buah Batu",
    "Kost Griya Citra Dayeuhkolot", "Kost Buah Batu Mandiri 2", "Kost Green Buah Batu 3","Kost Dayeuhkolot Prima 2", "Kost Buah Batu Sinar", "Kost Graha Harmoni Dayeuhkolot",
    "Kost Pondok Buah Batu 3", "Kost Dayeuhkolot Ceria 2", "Kost Taman Buah Batu 5","Kost Green Residence Dayeuhkolot", "Kost Buah Batu Maju", "Kost Dayeuhkolot Nirwana", "Kost AZ ciganitri", "Kost Irham", "Violet Kost Ciganitri "
]

kost_prices = [
 500000, 1075264, 979472, 1409875, 950886,
579993, 1112218, 1485122, 1011733, 1155473,
1250748, 1325251, 784247, 972659, 1458049,
813141, 1024778, 1345857, 808094, 1200997,
816381, 1192124, 1413639, 1392675, 1466311,
593306, 1375942, 1457962, 632406, 915785,
652943, 621994, 958171, 783751, 1136855,
1197256, 686718, 810035, 1116425, 673643,
1450226, 1279913, 1195994, 1496357, 1272370,
1089817, 556994, 755203, 607226, 842079,
532314, 962426, 562459, 1488629, 1472817,
1459456, 924933, 1150325, 776430, 1413360,
744020, 725181, 1112852, 1450261, 926966,
841430, 1004875, 1430824, 563682, 712051,
962436, 656600, 1054534, 1179759, 635510,
978628, 1161867, 950446, 767429, 1438856,
1446810, 917438, 1276954, 1401048,527575,
1112020,879418 ,869298 ,1099410 ,943515,
773077 ,1049481 ,881858 ,1340951 ,1355196 ,
1025454 ,1465513 ,1272100 ,590757 ,754933 ,
553501 ,1073591 ,1293165 ,965491 ,669952 ,
902934 ,1455136 ,1277636 ,589390 ,885872 ,
645362 ,680834 ,591697 ,728805 ,1099969 ,
1482490 ,535739 ,1355871 ,1092612 ,859483 ,
973138 ,1391086 ,1154015 ,1346211 ,1122737 ,
649340 ,1123966 ,777351 ,1084686 ,1102277 ,
957340 ,1135813 ,1418934 ,1059328 ,1155712 ,
1052568 ,751426 ,1368061 ,1087181 ,1254470 ,
541793 ,1239297 ,1051010 ,1353347 ,1194845 ,
1464524 ,882951 ,1078839 ,719371 ,637358 ,
1154292 ,1434003 ,1404129 ,1004630 ,517984 ,
1016853 ,679278 ,1369593 ,1381822 ,582559 ,
769122 ,684256 ,1494406 ,1295931 ,1071294 ,
1206283 ,1282557 ,1444309 ,1259000,1014485 ,
1360245 ,1190387 ,1147563 ,1394887 ,1460484 ,
1067449 ,1498670 ,1045840 ,1463806 ,1182987 ,
1368939 ,785552 ,1081852 ,742849 ,1387297 ,
626746 ,502983 ,750940 ,540226 ,1325302 ,
649984 ,1474078 ,1009332 ,1294476 ,609508 ,
1157035 ,1009049 ,1389074 ,744877 ,1090219 ,
777276 ,1079658 ,1098381 ,1486882 ,1334800 ,
1450586 ,1437028 ,1444494 ,699935 ,1096600 ,
1111592 ,1398539 ,766516 ,526220 ,864858 ,
607937 ,1493328 ,561058 ,994993 ,890206 ,
892491, 658355, 809072, 731068, 1104842,
564060, 813813, 723137, 1477814, 1302460,
885503, 696815, 759951, 1097740, 1149853,
1452591, 737947, 843721, 1272573, 974995,
1148619, 769026, 1161356, 1090569, 1421742,
1072394, 712146, 524132, 1340617, 675044,
533316, 734276, 786763, 1382692, 730481,
1055998, 1453019, 722072, 1331615, 520396,
1082910, 1179341, 1250022, 1208883, 985684,
1341340, 902243, 1378991, 1459589, 647919,
1255938, 1050588, 977699, 964553, 1246621,
1141372, 725995, 1029509, 1253053, 1270569,
672591, 709430, 1120454, 1436926, 744355,
936149, 887343, 1498937, 1436015, 1405199,
885147, 1241156, 515634, 624338, 824174,
799522, 1154735, 516786, 585028, 1094321,
1212293, 1134844, 1069204, 1428572, 975981,
1272422, 810881, 1268770, 1140421,569891,
942231 ,900959 ,1434358 ,1463156 ,1395554 ,
761563 ,891200 ,1298623 ,702983 ,862426 ,
1393693 ,1463395 ,1046345 ,1428911 ,616553 ,
591959 ,1375291 ,1338756 ,625095 ,1171676 ,
506458 ,1462180 ,1390016, 1298000,  500000, 1075264, 979472, 1409875, 950886,
579993, 1112218, 1485122, 1011733, 1155473,
1250748, 1325251, 784247, 972659, 1458049,
813141, 1024778, 1345857, 808094, 1200997,
816381, 1192124, 1413639, 1392675, 1466311,
593306, 1375942, 1457962, 632406, 915785,
652943, 621994, 958171, 783751, 1136855,
1197256, 686718, 810035, 1116425, 673643,
1450226, 1279913, 1195994, 1496357, 1272370,
1089817, 556994, 755203, 607226, 842079,
532314, 962426, 562459, 1488629, 1472817,
1459456, 924933, 1150325, 776430, 1413360,
744020, 725181, 1112852, 1450261, 926966,
841430, 1004875, 1430824, 563682, 712051,
962436, 656600, 1054534, 1179759, 635510,
978628, 1161867, 950446, 767429, 1438856,
1446810, 917438, 1276954, 1401048,527575,
1112020,879418 ,869298 ,1099410 ,943515,
773077 ,1049481 ,881858 ,1340951 ,1355196 ,
1025454 ,1465513 ,1272100 ,590757 ,754933 ,
553501 ,1073591 ,1293165 ,965491 ,669952 ,
902934 ,1455136 ,1277636 ,589390 ,885872 ,
645362 ,680834 ,591697 ,728805 ,1099969 ,
1482490 ,535739 ,1355871 ,1092612 ,859483 ,
973138 ,1391086 ,1154015 ,1346211 ,1122737 ,
649340 ,1123966 ,777351 ,1084686 ,1102277 ,
957340 ,1135813 ,1418934 ,1059328 ,1155712 ,
1052568 ,751426 ,1368061 ,1087181 ,1254470 ,
541793 ,1239297 ,1051010 ,1353347 ,1194845 ,
1464524 ,882951 ,1078839 ,719371 ,637358 ,
1154292 ,1434003 ,1404129 ,1004630 ,517984 ,
1016853 ,679278 ,1369593 ,1381822 ,582559 ,
769122 ,684256 ,1494406 ,1295931 ,1071294 ,
1206283 ,1282557 ,1444309 ,1259000,1014485 ,
1360245 ,1190387 ,1147563 ,1394887 ,1460484 ,
1067449 ,1498670 ,1045840 ,1463806 ,1182987 ,
1368939 ,785552 ,1081852 ,742849 ,1387297 ,
626746 ,502983 ,750940 ,540226 ,1325302 ,
649984 ,1474078 ,1009332 ,1294476 ,609508 ,
1157035 ,1009049 ,1389074 ,744877 ,1090219 ,
777276 ,1079658 ,1098381 ,1486882 ,1334800 ,
1450586 ,1437028 ,1444494 ,699935 ,1096600 ,
1111592 ,1398539 ,766516 ,526220 ,864858 ,
607937 ,1493328 ,561058 ,994993 ,890206 ,
892491, 658355, 809072, 731068, 1104842,
564060, 813813, 723137, 1477814, 1302460,
885503, 696815, 759951, 1097740, 1149853,
1452591, 737947, 843721, 1272573, 974995,
1148619, 769026, 1161356, 1090569, 1421742,
1072394, 712146, 524132, 1340617, 675044,
533316, 734276, 786763, 1382692, 730481,
1055998, 1453019, 722072, 1331615, 520396,
1082910, 1179341, 1250022, 1208883, 985684,
1341340, 902243, 1378991, 1459589, 647919,
1255938, 1050588, 977699, 964553, 1246621,
1141372, 725995, 1029509, 1253053, 1270569,
672591, 709430, 1120454, 1436926, 744355,
936149, 887343, 1498937, 1436015, 1405199,
885147, 1241156, 515634, 624338, 824174,
799522, 1154735, 516786, 585028, 1094321,
1212293, 1134844, 1069204, 1428572, 975981,
1272422, 810881, 1268770, 1140421,569891,
942231 ,900959 ,1434358 ,1463156 ,1395554 ,
761563 ,891200 ,1298623 ,702983 ,862426 ,
1393693 ,1463395 ,1046345 ,1428911 ,616553 ,
591959 ,1375291 ,1338756 ,625095 ,1171676 ,
506458 ,1462180 ,1390016, 4250000, 5296000
]


def measure_time_iterative(arr, target):
    start_time = time.perf_counter()
    iteratifAlgo(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

def measure_time_recursive(arr, target):
    start_time = time.perf_counter()
    rekursif_sequential_search(arr, target, 0)
    end_time = time.perf_counter()
    return end_time - start_time

def average_time(func, arr, target, repetitions=10):
    total_time = 0
    for _ in range(repetitions):
        total_time += func(arr, target)
    return total_time / repetitions

try:
    print("-------------------------------------------------")
    print("           Aplikasi Pencari Harga Kost           ")
    print("-------------------------------------------------")
    target_price = int(input("Masukkan harga kost yang ingin dicari: "))
except ValueError:
    print("Input tidak valid. Menggunakan harga default: 1000000")
    target_price = 1000000

default_price = 1000000
if target_price not in kost_prices:
    print("Harga tidak ditemukan. Menggunakan harga default: 1000000")
    target_price = default_price

index_found = iteratifAlgo(kost_prices, target_price)
if index_found != -1:
    print(f"Nama kost dengan harga {target_price}: {kost_list[index_found]} ditemukan pada index ke - {index_found + 1}")
else:
    print("Kost dengan harga tersebut tidak ditemukan.")

# Data untuk grafik
sizes = sorted(list(range(10, len(kost_prices) + 1, 500)))
iterative_times = []
recursive_times = []

for size in sizes:
    sublist_prices = kost_prices[:size]
    iterative_times.append(average_time(measure_time_iterative, sublist_prices, target_price))
    recursive_times.append(average_time(measure_time_recursive, sublist_prices, target_price))

plt.figure(figsize=(10, 6))
plt.plot(sizes, iterative_times, label="Iteratif", color="blue")
plt.ylabel("Waktu eksekusi(detik)", fontsize=12)
plt.title("Kompleksitas Waktu Algoritma Iteratif", fontsize=14)  
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sizes, recursive_times, label="Rekursif", color="green")
plt.ylabel("Waktu eksekusi(detik)", fontsize=12)
plt.title("Kompleksitas Waktu Algoritma rekursif", fontsize=14) 
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sizes, iterative_times, label="Iteratif", color="blue")
plt.plot(sizes, recursive_times, label="Rekursif", color="green")
plt.ylabel("Waktu eksekusi(detik)", fontsize=12)
plt.title("Kompleksitas Waktu Algoritma Iteratif vs algoritma rekursif", fontsize=14) 
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
