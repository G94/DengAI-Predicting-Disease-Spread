""" 
Copyright (c) 2020 Voxiva.
"""

### RENAME DATASETS
####################################################################
####################################################################
cols_rename_dev = ['Op', 'Fecha','OpDocOrigen', 'FechaDocOrigen', 'Observaciones', 'Pagado',
    'Financiado','ID_NaturalezaGastoIngreso', 'NaturalezaGastoIngresoNiv03_Nombre',
    'agenda_id','cliente_nombre', 'cliente_tipo_id','cliente_tipo','sucursal_id', 'sucursal_nombre', 'Kardex', 'codigo',
    'sku_descripcion','sku_unidad', 'id_unidad_gestion', 'Cantidad_dev', 'precio_dev',
    'descuento','descuento_valor', 'importe_dev']


### COLS KEEP
static_col = ['und_producto', 'Fecha_Month']
cols_dev = ["OpDocOrigen","Kardex", "Cantidad_dev", "precio_dev", "importe_dev"]


#### COLS TO FILL
####################################################################
####################################################################
list_number_static = ["Precio_getFirst", "Precio_getLast", "Precio_mean","Precio_amin",'Precio_amax']

list_number_dynamic = ["Importe_sum", "devuelto_sum", "Cantidad_sum",'Cantidad_dev_sum',
                    'origen_zona_id_get_unique','FormaPago_get_unique',
                    'RUC_get_unique', 'destino_zona_id_get_unique']

cols_fill = ['count_ALMACEN AREQUIPA', 'count_ALMACEN CHICLAYO',
    'count_ALMACEN CHIMBOTE', 'count_ALMACEN CUSCO',
    'count_ALMACEN GALLINAS SUPERMERCADOS', 'count_ALMACEN HUANCAYO',
    'count_ALMACEN HUANUCO', 'count_ALMACEN ICA', 'count_ALMACEN PIURA',
    'count_ALMACEN PUCALLPA', 'count_ALMACEN RAYZA Y HERMANOS BENEFICIO',
    'count_ALMACEN SUPERMERCADOS', 'count_ALMACEN TRUJILLO',
    'count_CHINCHA ALMACEN VENTAS', 'count_DESPACHOS CHINCHA ALMACEN',
    'count_LIMA ALMACEN GENERAL']



#### COLUMNS TO LAG
####################################################################
####################################################################
cols_lagging = ['Huevo_calato', 'Precio_estandarizado',  
                'CantidadNeto', 'PrecioDiff',  
                'Precio_amin', 'Precio_mean', 
                'Precio_getLast', 'Precio_getFirst',
                'destino_zona_id_get_unique', 
                'RUC_get_unique', 'total_almacen',
                'Importe_sum' ,  'Cantidad_sum',  'Cantidad_dev_sum', 
                'precio_minagri', 'Price_mean', 
                'Tasa_dif','PCT_change_sum' , 'Int_Huevo_calato',
    'Decimal_Huevo_calato', 'diff_int_mgr_pr', 'diff_decimal_mgr_pr',
    'diff_int_mgr_hc', 'diff_decimal_mgr_hc'] + cols_fill



##### FEATURES TO TRAIN ###############################################
####################################################################
####################################################################
cols_lagg = ['Huevo_calato_1', 'Huevo_calato_2',
       'Huevo_calato_3', 'Precio_estandarizado_1',
       'Precio_estandarizado_2', 'Precio_estandarizado_3',
#        'CantidadNeto_1', 'CantidadNeto_2', 'CantidadNeto_3',
       'PrecioDiff_1', 'PrecioDiff_2', 'PrecioDiff_3', 'Precio_amin_1',
       'Precio_amin_2', 'Precio_amin_3', 'Precio_mean_1', 'Precio_mean_2',
       'Precio_mean_3', 'Precio_getLast_1', 'Precio_getLast_2',
       'Precio_getLast_3', 'Precio_getFirst_1', 'Precio_getFirst_2',
       'Precio_getFirst_3', 'destino_zona_id_get_unique_1',
       'destino_zona_id_get_unique_2', 'destino_zona_id_get_unique_3',
       'RUC_get_unique_1', 'RUC_get_unique_2', 'RUC_get_unique_3',
        'total_almacen_1', 'total_almacen_2', 'total_almacen_3',
#        'Importe_sum_1', 'Importe_sum_2', 'Importe_sum_3',
#        'Cantidad_sum_1', 'Cantidad_sum_2', 'Cantidad_sum_3',
#        'Cantidad_dev_sum_1', 'Cantidad_dev_sum_2', 'Cantidad_dev_sum_3',
       'precio_minagri_1', 'precio_minagri_2', 'precio_minagri_3',
       'Price_mean_1', 'Price_mean_2', 'Price_mean_3', 'Tasa_dif_1',
       'Tasa_dif_2', 'Tasa_dif_3', 'PCT_change_sum_1', 'PCT_change_sum_2',
       'PCT_change_sum_3', 'Int_Huevo_calato_1', 'Int_Huevo_calato_2',
       'Int_Huevo_calato_3', 'Decimal_Huevo_calato_1',
       'Decimal_Huevo_calato_2', 'Decimal_Huevo_calato_3',
       'diff_int_mgr_pr_1', 'diff_int_mgr_pr_2', 'diff_int_mgr_pr_3',
       'diff_decimal_mgr_pr_1', 'diff_decimal_mgr_pr_2',
       'diff_decimal_mgr_pr_3', 'diff_int_mgr_hc_1', 'diff_int_mgr_hc_2',
       'diff_int_mgr_hc_3', 'diff_decimal_mgr_hc_1',
       'diff_decimal_mgr_hc_2', 'diff_decimal_mgr_hc_3',
       'CantidadNeto_2_3',
       'Cantidad_sum_2_3']

cols_laggv2 = [i for i in cols_lagg if i[-1]!= "1" ]
cols_train = cols_laggv2 + static_col



##### COLS PREDICTIONS ###############################################
####################################################################
####################################################################
cols_predictions = ["Fecha", "Cliente", "Kardex", "Descripcion", "CantidadPred"]       