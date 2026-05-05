import pandas as pd


class QLNV:
    def __init__(self, file_path, title=[]):
        self.file_path = file_path
        self.title = title

    def timkiem(self, title_keyword, keyword):
        data = pd.read_csv(self.file_path)
        if self.title:
            data = data[self.title]
        result = data[data[title_keyword].astype(str).str.contains(keyword)]
        return [result.iloc[i].to_dict() for i in range(len(result))]
    def xoa(self,title_keyword, keyword):
        data = pd.read_csv(self.file_path)
        if self.title:
            data = data[self.title]
        result = data[~data[title_keyword].astype(str).str.contains(keyword)]
        result.to_csv(self.file_path, index=False)
        return True
    def capnhat(self, title_keyword, keyword, title_edit = [], new_data=[]):
        data = pd.read_csv(self.file_path)
        if self.title:
            data = data[self.title]
        for i in title_edit:
            data.loc[data[title_keyword].astype(str).str.contains(keyword), i] = new_data[title_edit.index(i)]
        data.to_csv(self.file_path, index=False)
        return True
    def them(self, new_data):
        data = pd.read_csv(self.file_path)
        if self.title:
            data = data[self.title]
        new_row = pd.DataFrame([new_data], columns=self.title)
        data = pd.concat([data, new_row], ignore_index=True)
        data.to_csv(self.file_path, index=False)
        return True