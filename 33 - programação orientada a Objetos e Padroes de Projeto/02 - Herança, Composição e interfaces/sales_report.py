from abc import ABC, abstractmethod
import gzip
import json

class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        """
        Aqui colocamos a lógica para a entidade 'se criar',
        ou seja, criar um relatório imprimível. Por simplicidade,
        vamos omitir essa lógica nos exemplos!
        SalesReportJSON(SalesReport) . A lógica é: class MinhaClasseHerdeira(ClasseAscendente)
        """
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]
    def compress(self):
        binary_content = json.dumps(self.build()).encode('utf-8')

        with gzip.open(self.export_file + '.gz','wb') as compressed_file:
            compressed_file.write(binary_content)

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):

    def serialize(self):
        # Vamos gerar, aqui, o nosso relatório em formato JSON
        with open(self.export_file + '.json', "w") as file:
            json.dump(self.build(), file)

class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass