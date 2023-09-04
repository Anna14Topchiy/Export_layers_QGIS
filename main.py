from qgis.core import QgsProject, QgsVectorLayerExporter

# Укажите путь к папке, в которую вы хотите экспортировать слои
output_folder = 'C:\\Users\\annat\\OneDrive\\GB\\Drumsheds\\test_scripts'

# Получите текущий проект QGIS
project = QgsProject.instance()

# Получите список всех слоев в проекте
layers = project.mapLayers().values()

# Переберите слои и экспортируйте их
for layer in layers:
    # Проверьте, является ли слой векторным
    if layer.type() == QgsMapLayer.VectorLayer:
        # Формируем имя файла для экспорта (например, имя слоя + ".shp")
        export_name = f'{output_folder}{layer.name()}.shp'

        # Определите параметры экспорта (например, формат, CRS)
        export_options = QgsVectorLayerExporter.ExportVectorFileOptions()
        export_options.actionOnExistingFile = QgsVectorLayerExporter.CreateOrOverwriteFile
        export_options.fileEncoding = "UTF-8"
        export_options.driverName = "ESRI Shapefile"
        export_options.layerOptions = QgsVectorLayerExporter.LayerOptions()
        export_options.layerOptions.setSkipAttributeCreation(False)

        # Устанавливаем проекцию 4326 (WGS 84)
        export_options.destinationCrs = QgsCoordinateReferenceSystem('EPSG:4326')

        # Выполните экспорт
        result, error_message = QgsVectorLayerExporter.exportLayer(layer, export_name, export_options)

        if result == QgsVectorLayerExporter.NoError:
            print(f'Слой {layer.name()} успешно экспортирован в {export_name}')
        else:
            print(f'Ошибка экспорта слоя {layer.name()}: {error_message}')

