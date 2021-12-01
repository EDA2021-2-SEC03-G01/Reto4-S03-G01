﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadServices(analyzer, airportsfile, routesfile, citiesfile):
    airportsfile = cf.data_dir + airportsfile
    input_airportsfile = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    for airport in input_airportsfile:
        model.addAirport(analyzer, airport)

    routesfile = cf.data_dir + routesfile
    input_routesfile = csv.DictReader(open(routesfile, encoding="utf-8"),
                                delimiter=",")
    for route in input_routesfile:
        model.addConnections(analyzer, route)

    citiesfile = cf.data_dir + citiesfile
    input_citiesfile = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    for city in input_citiesfile:
        model.addCiudad(analyzer, city)
    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def totalAirports(analyzer):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return model.totalAirports(analyzer)

def totalRoutes(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return model.totalRoutes(analyzer)

def totalCities(analyzer):
    """
    Retorna el total de ciudades
    """
    return model.totalCities(analyzer)

def infoPrimerAeropuerto(analyzer):
    return model.infoPrimerAeropuerto(analyzer)

def infoUltimaCiudad(analyzer):
    return model.infoUltimaCiudad(analyzer)

def req_1(analyzer):
    (lista_mayores, mayor) = model.req_1(analyzer)
    return (lista_mayores, mayor)