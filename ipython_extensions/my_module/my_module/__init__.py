
# import random
# from IPython.core.magic import magics_class, line_magic, Magics

# random.seed(123456)


# def generate_random.randint(0, max)


# @magics_class
# class RandomInt(Magics):

#     @line_magic
#     def random_int(self, line=''):
#         """Show information about versions of modules.
#         Usage:
#             %random_int [optional max - else max=100]
#         """

#         # try:
#         #     max = int(line)
#         # except:
#         #     max = 100
#         # self.nb = generate_rnd_int(max=max)
#         self.nb = 22

#         return self

#     def _repr_html_(self):

#         html = "<b>"
#         html += self.nb
#         html += "</b>"

#         return html


def _jupyter_server_extension_paths():
    return [{
        "module": "my_module"
    }]


def load_jupyter_server_extension(nbapp):
    print('toto')
    # nbapp.register_magics(RandomInt)
    nbapp.log.info("my_module enabled")
