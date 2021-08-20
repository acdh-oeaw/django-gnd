$(".custom-select").select2({
    ajax: {
      url: "https://lobid.org/gnd/search?format=json%3Asuggest",
      dataType: 'json',
      delay: 250,
      data: function (params) {
        return {
          q: params.term, // search term
          size: 100
        };
      },
      processResults: function (data) {

        return {
          results: data,
        };
      },
      cache: true,
    },
    minimumInputLength: 3,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection
  });
  
  function formatRepo (repo) {
    if (repo.loading) {
      return repo.label;
    }
  
    var $container = $(
      `<div class='select2-result-repository clearfix'>
          <div>${repo.label}</div>
          <div>${repo.id}</div>
          <h6><span class='badge badge-secondary'>${repo.category}</span></h4>
      </div>`
    );
    return $container;
  }
  
  function formatRepoSelection (repo) {
    let result;
    if (repo.id === '') {
      result = repo.text
    } else {
      result = `${repo.label} || ${repo.category} || ${repo.id}`
    }
    return result
  }