from scraperx import run, BaseDispatch, BaseDownload, BaseExtract


class Dispatch(BaseDispatch):

    def create_tasks(self):
        """Returns a single or a list of tasks to be downloaded

        The keys in the task can be anything that you want to be passed along
        to be used at different steps in the scraper. There are a few built-in
        keys that will be used behind the scenes if set.

        Built-ins:

            headers {dict} --
                Custom headers to use when downloading. If no `User-Agent` is
                set one will be set automatically to a random browser.

            proxy {str} --
                Use a specific proxy for this request. If not set, a random
                proxy will be used from the `PROXY_FILE` if one was set

            proxy_country {str} --
                2 letter country code. Used when selecting a proxy from
                `PROXY_FILE` if set

            device_type {str} --
                Options are `desktop` or `mobile`. Default is `desktop`.
                If no `User-Agent` is set in the headers key, this will be
                used when selecting the type of User-Agent to use.

        """
        return {'url': 'http://testing-ground.scraping.pro/blocks'}


class Download(BaseDownload):

    def download(self):
        return self.request_get(self.task['url']).write_file().save(self)


class Extract(BaseExtract):

    def extract(self, raw_source, source_idx):
        """Returns a single or a list of extractors

        In each extractor that is returned, the possiable fields are:

        Required:
            name {str} --
                Used to define the extractor. Will be available as
                `extractor_name` for use in the `file_template`

            selectors {list of str} --
                List of css selectors to use to select the content to pass to
                the extractor. If parsing non html content and `raw_source`
                is set, then this is NOT required.

            callback {function} --
                The extract method that will be called for each element
                that the selectors find.

        Optional:
            save_as {str} --
                Format to save the extracted data as.
                Current options are: `json`, `json_lines`.

            raw_source {str} --
                If source is `html`:
                    Used if you need to modify the source before the selectors
                    are run on it. Normally not needed.
                If source is not `html`, i.e. json/plain text/...:
                    In this case do NOT pass `selectors', but set `raw_source`
                    to a list of things to be passed to the `callback`.

            idx_offset {int} --
                The index of the item that the `callback` is currently
                processing. If not set, it will start at 0.

            file_name_vars {dict} --
                Additional variables that can be used in the `file_template`

            qa {dict} -- TODO: link to qa docs.

        Arguments:
            raw_source {str} -- Content from the source file.
            source_idx {int} -- Index of the source file that was downloaded.
        """
        return {'name': 'products',
                'selectors': ['#case1 > div:not(.ads)'],
                'callback': self.extract_product,
                'save_as': 'json',
                }

    def extract_product(self, element, idx, **kwargs):
        return {'title': element.css('div.name').xpath('string()').extract_first()}


if __name__ == '__main__':
    run(Dispatch, Download, Extract)
