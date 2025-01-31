from django.db.models.query import ValuesQuerySet
from django.conf import settings

    
class PageHeader(object):
    ''' 
    propriedades:
       style : Estilo a ser apresentado pela PageHeader
       components : Componentes que deverão integrar a PageHeader. É uma lista de dicts.
           Os dicts podem conter:
               type : Tipo do element. Atualmente se aceita "p" - Parágrafo, "label" - label, "div" - div
               name : nome do component
               text : Texto a ser apresentado
               style : formatação css para o component
    '''
    def __init__(self):
        self.style = str()
        self.components = []

    def set_style(self, style):
    	self.style = style

    def add_component(self, type, name, text = str(), style = str()):
        if not type in ("p", "label", "div"):
            raise "Parameter type is inválid. Parameter accept only p, label and div."

        if name.strip() == "":
            raise "Parameter name is inválid. Please insert a válid name."
        
        self.components.append({"type" : str(type), "name" : str(name), "text" : str(text), "style": str(style)})

class PageFooter(object):
    ''' 
    propriedades:
       style : Estilo a ser apresentado pela PageHeader
       components : Componentes que deverão integrar a PageHeader. É uma lista de dicts.
           Os dicts podem conter:
               type : Tipo do element. Atualmente se aceita "p" - Parágrafo, "label" - label, "div" - div
               name : nome do component
               text : Texto a ser apresentado
               style : formatação css para o component
    '''
    def __init__(self):
        self.style = str()
        self.components = []

    def set_style(self, style):
    	self.style = style

    def add_component(self, type, name, text = str(), style = str()):
        if not type in ("p", "label", "div"):
            raise "Parameter type is inválid. Parameter accept only p, label and div."

        if name.strip() == "":
            raise "Parameter name is inválid. Please insert a válid name."
        
        self.components.append({"type" : str(type), "name" : str(name), "text" : str(text), "style": str(style)})


class BandDataBase(object):
    def add_component(self, type, name, db_link, style = str()):
        if not type in ("dataP", "dataLabel", "dataDiv"):
            raise "Parameter type is inválid. Parameter accept only dataP, dataLabel and dataDiv."        
        
        if name.strip() == "":
            raise "Parameter name is inválid. Please insert a válid name."
        
        if db_link.strip() == "":
            raise "Parameter dbLink is inválid. Please insert the field's name that belongs to the query"
        try:
            self.components.append({"type" : str(type), "name" : str(name), "dbLink" : str(db_link), 
            	"style": str(style)})
        except Exception as e:            
            print(e)

    def set_style(self, style):
    	self.style = style
    


class MasterBand(BandDataBase):
    '''
        propriedades:
        style : Estilo a ser apresentado pela MasterPage
        components : Componentes que deverão integrar a MasterPage. É uma lista de dicts.
            Os dicts podem conter:
                type : Tipo do element. Atualmente se aceita "dataP" - Parágrafo buscando do dataBand, 
                      "dataLabel" - label buscand do dataBand, "dataDiv" - div buscando do dataBand
                name : nome do component
                dbLink : valor do campo a ser buscado no dataBand
                style : formatação css para o component
                detail: uma banda detalhe com 
          query = QuerySet com os dados que serão passados para o dataBand 
    '''
    def __init__(self):
        self.style = str()
        self.components = []
        self.query = None


#    def add_component(self, type, name, db_link, style = str()):
#        if not type in ("dataP", "dataLabel", "dataDiv"):
#            raise "Parameter type is inválid. Parameter accept only dataP, dataLabel and dataDiv."        
#        
#        if name.strip() == "":
#            raise "Parameter name is inválid. Please insert a válid name."
#        
#        if db_link.strip() == "":
#            raise "Parameter dbLink is inválid. Please insert the field's name that belongs to the query"
#        try:
#            self.components.append({"type" : str(type), "name" : str(name), "dbLink" : str(db_link), 
#            	"style": str(style)})
#        except Exception as e:            
#            print(e)
    

class GroupHeader(BandDataBase):
    def __init__(self, field_group):
        self.style = str()
        self.components = []
        self.field_group = field_group
        
    


class Report(object):
    ''' classe responsável por geração de relatórios básicos '''
    
    def __init__(self, page_header, master_band, template, page_title, page_footer=None, group_headers=[]):
        self.page_header = page_header
        self.master_band = master_band
        self.group_headers = group_headers
        self.page_footer = page_footer
        self.template = template        
        self.page_title = page_title

    def get_page_header(self):       
        return { "style": self.page_header.style, "components" : self.page_header.components}

    def get_page_footer(self):
        if self.page_footer:
            return { "style": self.page_footer.style, "components" : self.page_footer.components}
        else:
            return {}
    
    def get_group_headers(self):
        r = []
        group_header = None
        if self.group_headers:
            for group_header in self.group_headers:
                r.append({"style":group_header.style, "components": group_header.components, "field_group":group_header.field_group})
        else:
            return []
        
        return r
    
        
    def get_master_band_data(self):
        data = []
        row = []
        if self.master_band.query:
            
            #if str(self.master_band.query.__class__) !=  str(ValuesQuerySet):
            #    raise Exception("Property 'query' must be a 'django.db.models.query.ValuesQuerySet class'.")
                        
            for val in self.master_band.query:
                row = []
                for k in val.keys():
                    if val[k]:
                        row.append({"name": k, "value": val[k]})
                    else:
                        row.append({"name": k, "value": ""})
                data.append(row)   	
            
            return data
        else:
            return []

    def get_rel_configuration(self):
        return "data = { pageHeader:%s, pageFooter:%s, masterBand:{style:'%s', "\
        "components:%s, bandData:%s, groupHeaders:%s} }" % (self.get_page_header(), self.get_page_footer(), self.master_band.style, 
            self.master_band.components, self.get_master_band_data(), self.get_group_headers()) 

    def as_html(self):

        html = \
           ''' <!DOCTYPE html>
            <html> 
             <head> 
                <title>%s</title> 
                <meta charset="UTF-8">
                <script type="text/javascript" src="%scomponents/jquery/dist/jquery.min.js" charset="UTF-8"></script> 
                <script type="text/javascript" src="%sjs/vmsis-lib.js" charset="UTF-8"></script> 
                <script type="text/javascript" src="%svReport/vReport.js" charset="UTF-8"></script> 
              </head> 
              <body class="vReport"> 
              </body> 
                <script > 
                  (function(){ 
                    novo_relatorio = function(){ 
                      %s   
                      report = new vReport("A4 portrait", "body", data);   
                      report.view(); 
                    }; 
                    window.addEventListener("load", novo_relatorio, true);  
                  })() 
                </script>             
            </html>   ''' % (self.page_title, settings.STATIC_URL, settings.STATIC_URL, settings.STATIC_URL, self.get_rel_configuration())
        
        return html