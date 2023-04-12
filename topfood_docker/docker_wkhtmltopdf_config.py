# import docker
#
#
# client = docker.from_env()
# input_file = "/Users/katerinalazarenko/katrin_projects/topfood/templates/check_template.html"
# output_file = "/Users/katerinalazarenko/katrin_projects/topfood/media/pdf/file.pdf"
# container = client.containers.run(
#     "madnight/docker-alpine-wkhtmltopdf",
#     command=["wkhtmltopdf", "input_file", "output_file"],
#     remove=True,
#     volumes={
#         input_file: {"bind": "templates/check_template.html", "mode": "ro"},
#         output_file: {"bind": "media/pdf/file.pdf", "mode": "rw"}
#     }
# )
# with open(output_file, 'wb') as f:
#     f.write(container.logs(stdout=True, stderr=False))
